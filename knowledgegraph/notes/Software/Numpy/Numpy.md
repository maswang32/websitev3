# Numpy functions


## np.where

### With one argument
Returns indices where the condition is true

### With multiple arguments
Returns elements from one of two arrays, given a condition. For instance,
```dots = np.where(mask, dots, -np.inf)```
Returns dots where mask is True, otheriwse returns -np.inf