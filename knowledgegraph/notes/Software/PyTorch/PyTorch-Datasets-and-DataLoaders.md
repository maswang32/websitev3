# Datasets
- To make a torch Dataset, need to implement two functions:
    - __len__
    - __getitem__

```python
from torch.utils.data import Dataset


class SimpleDataset(Dataset):
    def __init__(self, x, y):
        self.x = torch.tensor(x).cuda()
        self.y = torch.tensor(y).cuda()
    
    def __len__(self):
        return len(self.y)
    
    def __getitem__(self, idx):
        return self.x[idx], self.y[idx]
```


# DataLoaders

```python
from torch.utils.data import DataLoader

dataset = SimpleDataset(x, y)

dataloader = DataLoader(dataset, batch_size=256, shuffle=True)
```


# Iteration
```
for batch in dataloader:
  batch_x,batch_y = batch
  batch_x = batch_x.to(device)
  batch_y = batch_y.to(device)
  ...
```

# Transforms
These let you pass in callables.


Last Reviewed: 8/14/2026