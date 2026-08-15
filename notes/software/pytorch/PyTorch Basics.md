# Defining a Network
```
  import torch
  import torch.nn as nn
  
  
  class MLP(nn.Module):
      def __init__(self, in_features=10, out_features=2, hidden_dim=32, num_hidden_layers=4):
          super().__init__()
          self.in_features = in_features
          self.out_features = out_features
          self.num_hidden_layers = num_hidden_layers
  
          if num_hidden_layers == 0:
              self.net = nn.Linear(in_features, out_features)
          else:
              layers = []
              layers.append(nn.Linear(in_features, hidden_dim))
              layers.append(nn.ReLU())
              
              for i in range(num_hidden_layers - 1):
                  layers.append(nn.Linear(hidden_dim, hidden_dim))
                  layers.append(nn.ReLU())
              layers.append(nn.Linear(hidden_dim, out_features))
              self.net = nn.Sequential(*layers)
  
      def forward(self, x):
          return self.net(x)
```

# Defining a Training Loop
Note that there are **5** essential operations inside the loop. Remember "FLZBO"
1. forward pass
2. loss computation
3. zero grad
4. backward pass
5. optimizer/weight update


There are **5** outside the loop. Remember MOLDT:
1. Defining the model (M)
2. Setting up the optimizer (O)
3. Defining the loss (L)
4. Sending the model and data to the device (D)
5. model.train() (T)


```
  # Device
  device = "cuda"

  # Create data
  y = torch.ones(1024,2)
  x = torch.randn(1024, 10)
  
  # Send data to device
  x = x.to(device)
  y = y.to(device)
  
  # Essential boilerplate for PyTorch
  model = MLP()
  model = model.to(device)
  optimizer = torch.optim.Adam(params=model.parameters(), lr=1e-4)
  loss_fcn = torch.nn.MSELoss()
  model.train()
  
  for i in range(100):


      pred = model(x)
      loss = loss_fcn(pred, y)
  
      optimizer.zero_grad()
      loss.backward()
      optimizer.step()
  
```


# Inference
Some layers work differently in eval mode. Also disable gradient tracking, which saves memory.
```
  model.eval()
  with torch.inference_mode(): # Faster than torch.no_grad()
    ...
```

# Datasets and DataLoaders
## DataLoaders
Wraps an iterable around a dataset:

```
  from torch.utils.data import TensorDataset, DataLoader
  
  dataset = TensorDataset(x,y)
  dataloader = DataLoader(dataset, batch_size=256, shuffle=True)
  
  for batch in dataloader:
    batch_x,batch_y = batch
    batch_x = batch_x.to(device)
    batch_y = batch_y.to(device)
    ...
```


# Saving and loading models
```
  torch.save(model.state_dict(), "model.pt")
  model.load_state_dict(torch.load("model.pt")) # optionally pass weights_only=False, weights_only=True is the default.
```