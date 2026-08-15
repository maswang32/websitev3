# DAG

## Recall this terminology on graphs
- A directed acyclic graph is a graph of nodes with directed edges (arrows) and no cycles.
- "Leaves" are nodes that have no arrows going out
- "Roots" are nodes that have no arrows going in


## How torch autograd works (summary)
When we do computations in PyTorch, we construct a directed acyclic graph. 
- The root of the graph is the output or loss, and the leaves of the graph are the inputs.
- Notice that the graph points backwards from the output to the inputs
- Following this graph allows us to do backpropagation.


## Torch autograd (more details)
When we do a tensor operation in PyTorch, it
 - Computes the result (a tensor)
 - Creates a grad_fn (assuming gradient tracking is enabled)


### What is a grad_fn?
- These grad_fns are nodes on a directed acyclic graph that pytorch constructs as we do operations. 
- They are associated with each operation we do.
- The output tensor of the operation stores a pointer to the grad_fn that produced it.
- They store the following things:  
  - Callable: the formula for the backwards pass, triggered by .backward().
      - Input: upstream gradient
      - Outputs: input gradients
  - Saved Tensors
      - These are needed for the backward pass
  - next_functions: three possibilities:
      - 1. Pointers to the grad_fn of the inputs.
      - 2. None (dead end), e.g. when you get to the input of your neural network, you don't care about the gradient normally
      - 3. AccumulateGrad, for when the input node is a leaf node with requires_grad=True. In this case, `grad` is populated (or accumulated) for the leaf node.
  


# Requires_grad
- When we create a tensor with `requires_grad=True``, like ``w = torch.randn(5,3, requires_grad=True)`, this tells us that we care about the gradient with respect to this tensor.
- Gradients are only available for **leaf** nodes of the computational graph, that also have requires_grad=True



# Computing Gradients - Example

```python
import torch

x = torch.ones(5)
w = torch.ones(5, 3, requires_grad=True)
b = torch.ones(3, requires_grad=True)

out = x @ w + b
loss = torch.sum(out**2)

# Backward pass
loss.backward()
print(w.grad)
print(x.grad)

# Print grad_fn
print(loss.grad_fn)
print(loss.grad_fn.next_functions)
print(out.grad_fn)
print(out.grad_fn.next_functions)

# These are None, since they are leaf nodes
print(x.grad_fn)
print(w.grad_fn)
print(b.grad_fn)
```

# Autograd functions
To define custom operations that support gradient tracking, torch has a special class called `torch.autograd.Function`. We can specify forward and backward passses for these functions, and they can enter the DAG when you call their apply() method.

This may be useful if your operation cannot be expressed in terms of other pytorch functions - you can now do whatever you want in the forward pass (use nondifferentiable or non-PyTorch functions) and simply specify how the backward pass should go.

The steps to doing this:

1. Subclass `torch.autograd.Function`
    1. Define two methods:
          1. forward()
              1. input: ctx, tensor(s)
              2. output: tensor or tuple of tensors
                  1. Use `ctx.save_for_backward(...)` to save a tensor or tuple of tensors, stored for computing the backward pass.
                      1. storing tensors here is good (instead of directly on context) since pytorch will clear them after backward() is called.
              3. Use `ctx.x = x` to save non-tensors for the backward pass
          2. backward() Defines the gradient formula
              1. inputs: grad_output - these are tensors, same as the number of outputs from forward.
                  1. DO NOT modify these in place.
              2. output: needs to be same number of arguments as the number of inputs to forward
                  1. Can return None for inputs that do not require gradient.
2. Does the function support double backward? If not, decorate backward() with `@once_differentiable()`
3. Validate gradients using grad_check

Linear Layer example
```python
import torch


class Linear(torch.autograd.Function):
    @staticmethod
    def forward(ctx, x, w, b):
        ctx.save_for_backward(x, w)
        return torch.einsum("nd,dk->nk", x, w) + b

    @staticmethod
    def backward(ctx, grad_output):
        x, w = ctx.saved_tensors
        dL_db = torch.sum(grad_output, dim=0)
        dL_dw = torch.einsum("nk,nd->dk", grad_output, x)
        dL_dx = torch.einsum("nk,dk->nd", grad_output, w)
        return dL_dx, dL_dw, dL_db
```


## Aside on setup_context()
Instead of passing ctx to forward, you can also have a setup_context() function that takes in ctx, inputs, and outputs, and calls save_for_backward().
 
Linear Layer Example, using `setup_context()`:
```python
import torch


class Linear(torch.autograd.Function):
    @staticmethod
    def forward(x, w, b):
        return torch.einsum("nd,dk->nk", x, w) + b

    @staticmethod
    def setup_context(ctx, inputs, outputs):
        x, w, _ = inputs
        ctx.save_for_backward(x, w)

    @staticmethod
    def backward(ctx, grad_output):
        x, w = ctx.saved_tensors
        dL_db = torch.sum(grad_output, dim=0)
        dL_dw = torch.einsum("nk,nd->dk", grad_output, x)
        dL_dx = torch.einsum("nk,dk->nd", grad_output, w)

        return dL_dx, dL_dw, dL_db


linear = Linear.apply
```


# Notes
## Lines of Code
- The DAG is agnostic to the names of variables
- The DAG is agnostic to 'lines of code' - something is added to the graph when a tracked tensor operation is called.

## Memory
- Even if you overwrite the same variable name several times (x = layer[i](x)), the tensor itself doesn't get overwritten - it remains in memory if it is going to be used for backward pass.
- The graph keeps these intermediate tensors alive. Backward frees the saved tensors, since they were only needed to compute the backward pass (unless retain_graph=True)
- Extra references can keep the graph alive and eat up memory (e.g. appending loss instead of loss.item())
- Need `retain_graph=True` if calling backwards more than once

## Detach
- `x.detach()` returns a new tensor that has the same data, but `requires_grad=False`, `grad_fn=None`, and is not part of the computational graph.

## torch.autograd.Function



# Sources
https://docs.pytorch.org/docs/2.13/notes/extending.html#extending-autograd


Last Reviewed: 8/14/2026