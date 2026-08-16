# Setup
- The forward pass is a linear layer with biasfollowed by a sigmoid.
- The loss is binary cross entropy loss (which is mean negative log likelihood)
- You have 
    - X (N,D) data matrix
    - w (D,) weight matrix
    - b (1,) bias matrix
    - y (N,) label


# Derivations
## Loss
The log likelihood of label $y_i$ is:
$$
\log(p(y_i)) = y_i\log(p_i) + (1-y_i)\log(1-p_i)
$$
Where $p_i$ is the ith output of the sigmoid. Note that the first term is active when the ground truth label is 1, and the second is active when it is zero.


The loss is the average negative log likelihood, or

$$
- \frac{1}{N} \sum_{i=1}^N \left[ \log(y_i) \right]
$$
$$
\boxed{= - \frac{1}{N} \sum_{i=1}^N \left[  y_i\log(p_i) + (1-y_i)\log(1-p_i) \right]}
$$
$$
= - \frac{1}{N} \sum_{i=1}^N \left[  y_i\log\left(\frac{1}{1+e^{-z_i}}\right) + (1-y_i)\log\left(1-\left(\frac{1}{1+e^{-z_i}}\right)\right) \right] 
$$
$$
= - \frac{1}{N} \sum_{i=1}^N \left[  -y_i\log\left(1+e^{-z_i}\right) + (1-y_i)\log\left(\frac{e^{-z_i}}{1+e^{-z_i}}\right)\right] 
$$
$$
= - \frac{1}{N} \sum_{i=1}^N \left[  -y_i\log\left(1+e^{-z_i}\right) + (1-y_i)\left[-z_i - \log\left(1+e^{-z_i}\right)\right]\right]
$$
$$
= - \frac{1}{N} \sum_{i=1}^N \left[  -y_i\log\left(1+e^{-z_i}\right) -z_i + y_iz_i - \log\left(1+e^{-z_i}\right) + y_i \log\left(1+e^{-z_i}\right) \right]
$$
$$
= \boxed{- \frac{1}{N} \sum_{i=1}^N \left[   -z_i + y_iz_i - \log\left(1+e^{-z_i}\right) \right]}
$$
## Derivative of loss with respect to logits
If we take the derivative of the loss with respect to a single entry in logit $z_k$, we get:
$$
\frac{\partial L}{\partial z_k} = \frac{\partial}{\partial z_k}\left(  - \frac{1}{N} \sum_{i=1}^N \left[   -z_i + y_iz_i - \log\left(1+e^{-z_i}\right) \right] \right)
$$
Only one term in the sum is relevant:
$$
\frac{\partial L}{\partial z_k} = \frac{\partial}{\partial z_k}\left(  - \frac{1}{N} \left[   -z_k + y_kz_k - \log\left(1+e^{-z_k}\right) \right] \right)
$$
$$
\frac{\partial L}{\partial z_k} =   - \frac{1}{N} \left[ -1 + y_k + \frac{e^{-z_k}}{\left(1+e^{-z_k}\right)} \right]
$$
$$
\frac{\partial L}{\partial z_k} =   - \frac{1}{N} \left[y_k - \frac{1}{\left(1+e^{-z_k}\right)} \right]
$$
$$
\frac{\partial L}{\partial z_k} =  \frac{1}{N} \left[ \frac{1}{\left(1+e^{-z_k}\right)}  - y_k \right]
$$
$$
\boxed{
\frac{\partial L}{\partial z_k} =  \frac{1}{N} \left[p_k  - y_k \right]}
$$
## Derivative of logits with respect to weights and biases
$$
z_k = x_{k1} w_1 + ... + x_{kD} w_D + b
$$
$$
\frac{\partial z_k}{\partial w_j} = x_{kj} 
$$
$$
\frac{\partial z_k}{\partial b} = 1 
$$
## Applying the chain rule
### Weight
$$
\frac{dL}{dw_j} = \sum_{k=1}^N \left[\frac{\partial L}{\partial z_k} \cdot \frac{\partial z_k}{\partial w_j} \right]
$$
$$
= \sum_{k=1}^N \frac{1}{N} \left[p_k  - y_k \right] x_{kj}
$$
We notice this is a matrix vector mulitplication across the $N$ axis. Since $X$ is $N \times D$, and $p-y$ is an $N$-vector, we have
$$
\boxed{
\frac{dL}{dw_j} = \frac{X^T (p - y)}{N}}
$$

### Bias
Using the chain rule again, we get:
$$
\frac{dL}{db}= \sum_{k=1}^N \frac{1}{N} \left[p_k  - y_k \right] 
$$


Last Reviewed: 08/16/2026