# Initializing a Tensor

```python
# From Nested Lists
data = [[1, 2], [3, 4]]
x = torch.tensor(data)

# From Numpy
data = np.array([[1, 2], [3, 4]])
x = torch.from_numpy(data)

# Random/Constant Values
x = torch.randn(10, 10)
x = torch.rand(10, 10)  # Uniform (0,1)

# From other tensors
x = torch.zeros_like(my_tensor)
x = torch.ones_like(my_tensor)
x = torch.rand_like(my_tensor)
x = torch.randn_like(my_tensor)


# With datatype/device
x = torch.randn(10, 10, dtype=torch.bfloat16, device="cuda:0")
```

# Tensor attributes:
```python
x.shape
x.dtype  # torch.float32
x.device
```


# Tensor Operations (incomplete)
- torch.stack - stacks tensors along a new axis
- torch.cat - concatenates tensors along an existing axis
- x.item() - converts a one element tensor to a scalar.
- x.add_(5) - adds 5 to each element in place (discouraged, errors if a value is overwritten that is needed for backprop)

## Matrix multiplication
```python
y1 = A @ A.T  # Method 1
y2 = A.matmul(A.T)  # Method 2

y3 = torch.randn_like(y1)  # Method3
torch.matmul(A, A.T, out=y3)
```

# Tensor and numpy arrays share underlying memory, if the tensor is on CPU
```python
x = torch.ones(5)
x_np = x.numpy()
x += 5
print(x_np)
x_np *= 2
print(x)
```

```python
x_np = np.ones((5))
x = torch.from_numpy(x_np)

x += 5
print(x_np)
x_np *= 2
print(x)
```

Last Reviewed: 8/14/2026