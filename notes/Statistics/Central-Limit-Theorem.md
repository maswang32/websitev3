# Central Limit Theorem
The distribution of the sample mean approaches a normal distribution with variance $\frac{Var(X)}{N}$, where $Var(X)$ is the variance of a single sample.

Formally, suppose we have 

$$
\bar{X}_n = \frac{X_1 + \cdots X_n}{n}
$$
Then as $n$ becomes large, $\bar{X}_n$ becomes approximately normally distributed. What are the mean and variance? Well, they must match up with our laws of expecation and variance:
- $E[\bar{X}_n] = E[X]$
- $Var(\bar{X}_n) = \frac{1}{N} Var(X)$

Equivalently, $\sigma_{\bar{X}} = \frac{\sigma_X}{\sqrt{N}}$.


# Law of Large Numbers
The sample mean approaches the true mean.


Last Reviewed: 08/16/2026