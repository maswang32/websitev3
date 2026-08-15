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


# Sources
https://docs.pytorch.org/docs/2.13/notes/extending.html#extending-autograd


Last Reviewed: 8/14/2026