
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


# Aside on setup_context()
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
