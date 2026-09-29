# Discrete Distributions
## Bernoulli
- Expectation: $p$
- Variance: $p(1-p)$

Variance is maximized at $p=0.5$

## Binomial:
- Expectation: $np$
- Variance: $np(1-p)$

This is the sum of Bernoullis, which is how we got the expectation and variance. It approximates a normal distribution of the same mean and variance when $n$ is large.

## Poisson
- Expectation = Variance = $\lambda$

This is the chance that a number of events happens in a fixed amount of time, e.g., the number of buses that arrive in 5 minutes, if the inter-arrival time between events is exponential.


# Continuous Distributions
## Uniform
- Expectation: $\frac{a + b}{2}$
- Variance: $\frac{(b-a)^2}{12}$

The expected maximum of $n$ draws from $U(0,1) = \frac{n}{n+1}$.

## Normal/Gaussian
- Expectation: $\mu$
- Variance: $\sigma^2$

68%, 95%, and 99.7% of the probability mass of a normal distribution is within 1, 2, and 3 standard deviations of the mean, respectively.

## Exponential
- Expectation: $\frac{1}{\lambda}$
- Variance: $\frac{1}{\lambda^2}$

Memoryless: $P(X > s + t | X > s) = P(X > t)$. Or the probability that $X$ occurs in the next $t$ seconds doesn't depend on how long we have waited so far.


Last Reviewed: 08/16/2026
