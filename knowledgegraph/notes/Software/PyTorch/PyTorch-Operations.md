
# Some Tensor Operations
- torch.stack - stacks tensors along a new axis
- torch.cat - concatenates tensors along an existing axis
- x.item() - converts a one element tensor to a scalar.
- x.add_(5) - adds 5 to each element in place (discouraged, errors if a value is overwritten that is needed for backprop)
- torch.clamp(x, min, max) - clamps the values in the tensor to minimum and maximum values
- torch.amax - equivalent to np.max
- torch.where - equivalent to np.where
- torch.einsum - equivlaent to np.einsum
- x.mT - swaps the last two dims
- @ - contracts last dim on left with second-to-last on right
- x.permute(0, 2, 3, 1)
    - "the new shape, described in old axis names"
    - The new shape is (old axis 0, old axis 2, old axis 3, old axis 1)

Also
- Use dim instead of axis
- keepdim instead of keepdims

