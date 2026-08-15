Modules are basically neural network layers or networks. Here are some examples of modules that come with PyTorch:

# Layers
- nn.Flatten()
- nn.Softmax(dim=-1)
- nn.ReLU()
- nn.Linear()
- nn.Sequential(*[list_of_layers])
    - This one is how I typically initialize say, an MLP

# Getting Parameters
```python
for name, param in model.named_parameters():
    print(name)
    print(param.size())
```
