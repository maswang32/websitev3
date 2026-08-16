# Technique 1: Explicit scalar derivatives
This technique works well for computing closed-form derivatives on paper.

## 1. Write the formula for one (scalar) output
For instance, for softmax, (ignoring the batch dimension), we have:
$$
p_i = \frac{e^{z_i}}{\sum_{k=1}^C e^{z_k}}
$$
## 2. Differentiate by each relevant (scalar) input
We are now interested in computing the derivative of the function's output with respect to its input(s), which may be activations or parameters.

For instance, for softmax, we compute
$$
\frac{\partial p_i}{\partial z_j}
$$
This specifies entry $(i,j)$ of the Jacobian matrix of partial derivatives.

For softmax, we get
$$
\frac{\partial p_i}{\partial z_j} = \frac{\delta_{ij}e^{z_j}}{S} - \frac{e^{z_j}}{S}\frac{e^{z_i}}{S}
$$
Where $S = \sum_{k=1}^C e^{z_k}$. Note that using the (Kronecker) delta function often allows us to consider the cases where $i=j$ and $i \neq j$ simultaneously. This simplifies to:

$$
\frac{\partial p_i}{\partial z_j} = \delta_{ij} p_i - p_ip_j
$$
## 3. Apply the chain rule, using the upstream gradient.
Assume we are given the derivative of the loss with respect to the output, in this case $\frac{\partial L}{\partial p_i}$ for each output $p_i$.

The law of total derivative (multivariable chain rule) states that the derivative of the loss with respect to any given input is:
$$
\frac{\partial L}{\partial z_j} = \sum_i \frac{\partial L}{\partial p_i} \frac{\partial p_i}{\partial z_j}
$$
Evaluating this dot product gives us our answer.
$$
\frac{\partial L}{\partial z_j} = \sum_i \frac{\partial L}{\partial p_i} \left[ \delta_{ij} p_i - p_ip_j \right]
$$
$$
= \frac{\partial L}{\partial p_j} p_j - p_j \sum_i \frac{\partial L}{\partial p_i} p_i
$$
$$
= p_j \left(\frac{\partial L}{\partial p_j} - \sum_i \frac{\partial L}{\partial p_i} p_i \right)
$$
This is our answer.

# Technique 2: Line-By-Line Technique
This technique is faster when doing live coding, and helps for stuff like batchnorm.


## Steps

1. Go line-by-line, in the forward pass. Try to limit the number of operations per line.
2. Number each line in the forward pass.
3. Starting from the last line in the forward pass and going backward, write the backwards operation(s) that correspond to each forward operation.
    1. If the forward is n inputs -> one output, that means the backwards has n lines: one for each input.
    2. Treat things like scalars when you can.
4. Specify what you need to store from the forward pass, and copy this to the backward pass.
    1. Tip: Look for everything that is not a derivative in the backwards pass - these are generally what you need to store from the forward pass.

## Example:
LayerNorm forward:
```python
N, D = x.shape
x_demeaned = x - np.mean(x, axis=-1, keepdims=True)  # Line 1

# Compute std
x_sumsq = np.sum(x_demeaned**2, axis=-1, keepdims=True)  # Line 2
x_var = x_sumsq / D  # Line 3
x_std = np.sqrt(x_var + eps)  # Line 4
x_std_inv = 1 / x_std  # Line 5

# Normalize
x_normed = x_demeaned * x_std_inv  # Line 6
return x_normed * gamma + beta, (
    gamma,
    eps,
    x_normed,
    x_demeaned,
    x_std_inv,
    x_std,
    x_var,
    x,
)  # Line 7
```
LayerNorm backward:
```python
gamma, eps, x_normed, x_demeaned, x_std_inv, x_std, x_var, x = cache
N, D = x_normed.shape

# Line 7
dL_dbeta = np.sum(dL_dy, axis=0)  # (N,D) -> (D,)
dL_dgamma = np.sum(dL_dy * x_normed, axis=0)  # (N,D) * (N,D) -> (D,)
dL_dx_normed = (
    dL_dy * gamma
)  # (N,D) * (D,) -> (N,D) (There is an equivalent pointwise operation)

# Line 6
dL_dx_std_inv = np.sum(
    dL_dx_normed * x_demeaned, axis=-1, keepdims=True
)  # (N,D) * (N,D) -> (N,1)
dL_dx_demeaned = dL_dx_normed * x_std_inv  # (N,D) * (N,1) -> (N,D)

# Line 5
dL_dx_std = dL_dx_std_inv * (-1 / x_std**2)  # (N,1) * (N,1) -> (N,1)

# Line 4
dL_dx_var = dL_dx_std * (0.5 / np.sqrt(x_var + eps))  # (N,1) * (N,1) -> (N,1)

# Line 3
dL_dx_sumsq = dL_dx_var / D  # (N,1) -> (N,1)

# Line 2
dL_dx_demeaned += dL_dx_sumsq * 2 * x_demeaned  # (N,1) * (N,D) -> (N,D)

# Line 1
dL_dx = dL_dx_demeaned - np.mean(dL_dx_demeaned, axis=-1, keepdims=True)

return dL_dx, dL_dgamma, dL_dbeta
```

# Tips
1. For normalization:
    1. For RMSNorm and Layernorm, the std and variance vectors are all (N,1) (one for each batch item).
2. If you multiply by a constant during the forwards pass, multiply by the same one during the backwards pass.
3. If you sum during forward, broadcast during the backward.
4. If you broadcast during forward, sum during backward. You can think of this two ways:
    1. When you broadcast something during forward, it affects many things which eventually affect the output, so its influence is multiplied.
    2. Visualize the backward flow of gradient through the network during backprop. When you broadcast during the forwards pass, you have the same input contributing to many output nodes. During the backwards pass, gradient from many output nodes "flow into" the same input node.



# Debugging
## 1. Make sure you are not using the wrong variable (e.g. sum_exp vs log_sum_exp)
This was an issue for me while doing softmax.

This was also an issue for me when doing attention - make sure you use the scaled dot product, don't reuse the non-scaled one by accident!



## 2. Make sure you are summing over the correct axis.
For instance, if the forward pass is this:
```python
x_normed = x_demeaned * x_std_inv  # (N,D) * (N,1)
return x_normed * gamma + beta  # (N,D) * (D,) + (D,)
```

The backwards pass for the last line is:
```python
dL_dbeta = np.sum(dL_dy, axis=0)  # (N,D) -> (D,)
dL_dgamma = np.sum(dL_dy * x_normed, axis=0)  # (N,D) * (N,D) -> (D,)
dL_dx_normed = dL_dy * gamma  # (N,D) * (D,) -> (N,D)
```

Note that dL_dbeta and dL_dgamma are summed over the batch dimension (axis 0), since they are broadcast across the batch dimension during the forward pass.

On the other hand, the backwards pass for the second-to-last line is this:
```python
dL_dx_std_inv = np.sum(
    dL_dx_normed * x_demeaned, axis=-1, keepdims=True
)  # (N,D) * (N,D) -> (N,1)
```
We sum across the model_dim axis (D,), since during the forward pass, std_inv is broadcast to all dimensions.





## 3. Consider the interaction between terms.
For instance, if this is the forward pass:
```python
x_demeaned = x - np.mean(x, axis=-1, keepdims=True)
```

This backward pass is incorrect:
```python
dL_dx = dL_dx_demeaned * (1 - 1 / D)
```

The correct backward pass is:
```python
dL_dx = dL_dx_demeaned - np.mean(dL_dx_demeaned, axis=-1, keepdims=True)
```

## 4. Make sure you accumulate gradients for inputs that contribute to multiple outputs.

# Conventions
It will be helpful to use a single-letter convention for different dimensions, to make einsums more readable.

## Attention/Transformers
We can use these single-letter labels for dimensions:
1. n = batch dimension
2. t = query time dimension
3. s = key time dimension
4. d = model dimension
5. k = query/key dimension
6. v = value dimension


This will mean
1. input is `ntd`
2. query projection is `dk`
3. key projection is `dk`
4. value projection is `dv`
5. query matrix is `ntk`
3. key matrix is `nsk`
4. value matrix is `nsv`
6. Attention, dot product, and scaled dot product matrices are `nts`
7. output matrix is `ntv`



# Hints/Things to remember
1. Softmax
    1. you only need to cache the output prob
2. Layernorm
    1. For layernorm, there are 7 lines of code in the forward pass
3. attention
    1. For cross attention and self attention, if there is a mask, you do not need to consider it on the backwards pass. The operation in the backward pass would be to zero out the gradient of `dL_dscores`. But dL_dscores is (according to the softmax backward) `probs * (dL_dprobs - dot)`, and multiplying by probs (which is the attention mask) already zeros it out.
    2. for the attention operation itself, you only need to cache query, key, value, and attention matrix.
    3. Don't forget to subtract max logits here



Last Reviewed: 8/14/2026