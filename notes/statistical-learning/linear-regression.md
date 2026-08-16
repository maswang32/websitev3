# Setup
- The forward pass is a linear layer with bias
- The loss is MSE loss (which is mean negative log likelihood under a gaussian distribution)
- You have 
    - X (N,D) data matrix
    - w (D,) weight matrix
    - b (1,) bias matrix
    - y (N,) label

We assume that, given some input, the linear layer outputs the mean of a gaussian distribution with some fixed standard deviation.

The probability of a ground truth label is evaluated against this gaussian distribution to determine the likelihood.

# Derivations
## Loss
The likelihood of label $y_i$ is:
$$
p(y_i) = C e^{\frac{-(y_i - \hat{y}_i)^2}{2\sigma^2}}
$$
For some normalizing constant $C$.

Maximizing the likelihood of the data is equivalent to maximizing the log likelihood of the data.

Since the likelihood of the data is the product of the likelihoods of individual datapoints, the log likelihood is the sum of the log likelihoods of individual datapoints.

Thus, maximizing the sum of the log likelihoods of individual datapoints also maximizes the likelihood of the data.

The sum of the log likelihoods of the data points:
$$
 = \sum_{i=1}^N \log\left(C e^{\frac{-(y_i - \hat{y}_i)^2}{2\sigma^2}}\right)
$$

This is also equivalent to minimizing the negative mean of the log likelihoods of the data points:
$$
 = -\frac{1}{N}\sum_{i=1}^N \log\left(C e^{\frac{-(y_i - \hat{y}_i)^2}{2\sigma^2}}\right)
$$
$$
 = -\frac{1}{N}\sum_{i=1}^N \log\left(C\right) + \frac{-(y_i - \hat{y}_i)^2}{2\sigma^2}
$$
We can ignore the normalizing constant without affecting the optimization problem:
$$
 = -\frac{1}{N}\sum_{i=1}^N \frac{-(y_i - \hat{y}_i)^2}{2\sigma^2}
$$
We can also ignore the denominator:
$$
 = -\frac{1}{N}\sum_{i=1}^N -(y_i - \hat{y}_i)^2
$$
$$
\boxed{
= \frac{1}{N}\sum_{i=1}^N (y_i - \hat{y}_i)^2
}
$$
And this is our MSE Loss.
## Derivative of Loss with respect to weights and bias
### Weights:
$$
\frac{\partial }{\partial w_j } \left[ \frac{1}{N}\sum_{i=1}^N (y_i - \hat{y}_i)^2 \right]
$$
$$
\frac{\partial }{\partial w_j } \left[ \frac{1}{N}\sum_{i=1}^N (\hat{y}_i - y_i)^2 \right]
$$
$$
= \frac{1}{N}\sum_{i=1}^N 2 (\hat{y}_i - y_i) \cdot \frac{\partial \hat{y}}{\partial w_j}
$$
$$
= \frac{1}{N}\sum_{i=1}^N 2 (\hat{y}_i - y_i) \cdot x_{ij}
$$
Or
$$
\boxed{\frac{\partial L}{\partial w} = \frac{2}{N} X^T (\hat{y} - y)}
$$

### Bias:
Replace the $x_{ij}$ with a $1$, since $\frac{\partial \hat{y}}{\partial b} = 1$:
$$
\boxed{\frac{\partial L}{\partial b } = \frac{1}{N}\sum_{i=1}^N 2 (\hat{y}_i - y_i)}
$$

Then we can proceed to optimize the weights and biases.

Last Reviewed: 8/16/2026