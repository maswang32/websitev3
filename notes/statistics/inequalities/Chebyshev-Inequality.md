- The probability of being far from the mean can't be too big.
- The variance must be a certain amount
    - (if we know some probability mass is far from the mean).

# Derivation
Let $X$ be a random variable and $\mu$ be its mean.

Then
$(X - \mu)^2$ is a non-negative random variable, and we can apply markov:

$$
P\left((X - \mu)^2 \geq y\right) \leq \frac{E[(X-
\mu)^2]}{y}
$$

$$
P\left(|X - \mu| \geq \sqrt{y}\right) \leq \frac{E[(X-
\mu)^2]}{y}
$$
Let $t = \sqrt{y}$
$$
P\left(|X - \mu| \geq t\right) \leq \frac{E[(X-
\mu)^2]}{t^2}
$$

$$
\boxed{
P\left(|X - \mu| \geq t\right) \leq \frac{Var(X)}{t^2}}
$$

# Intuition
- The probability that $X$ is $t$ from its mean cannot be too large. It is is bounded by its variance.
- Once again, $t$ is some arbitrary threshold (the inequality is true for all $t$).

## Visual Proof
Imagine splitting up the distribution into three segments:
1. Below $\mu - t$
2. Between $\mu - t$ and $\mu + t$
3. Above $\mu + t$

There is no upper limit to the variance, since the mass on segments 1 and 3 can go very far out.

There is a lower limit to the variance, if you push segments 1 and 3 torward the mean, and concentrate segment 2 at the mean. Then all the probability mass is at the mean, $mu-t$ and $mu+t$.

What is the variance in this case? It would be 
$$
P(X \leq \mu - t)t^2 + P(\mu - t < X < \mu + t) \times 0 + P(X \geq \mu + t)t^2
$$
Combining the first and third terms this is:
$$
P\left( (X \leq \mu - t) \cup (X \geq \mu + t)\right) t^2
$$
This is equivalent to
$$
P(|X - \mu| \geq t) t^2
$$
Which is a lower bound on the variance (or the variance is an upper bound on the above expression).


# Notes
- Need to know mean and variance
- Random variable doesn't have to be non-negative.
- For both Chebyshev and Markov, the Variance or Expectation must be greater than some probability.

# Applications
## Bounding Error
You can bound the distribution of the error (which can be positive or negative). Then you can say the probability of the error being greater than $t$ is bounded.

Last Reviewed: 08/17/2026