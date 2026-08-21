# Numpy functions


## np.where
Returns elements from one of two arrays, given a condition. For instance,
```dots = np.where(mask, dots, -np.inf)```
Returns dots where mask is True, otheriwse returns -np.inf