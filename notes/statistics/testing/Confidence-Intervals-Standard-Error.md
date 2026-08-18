# Introduction
Say you use 100 eval samples to evaluate your model, and produce a metric (e.g., 12.7), which is the average of per-example metrics.

Lets ask two questions:
1. If you had chosen different samples from the same eval distribution, you would have a different number. How much does this number wobble with the choice of the eval set?
2. We are actually interested in the model's performance on the eval **distribution**, not just these 100 eval examples. What can we say about the model's performance on the eval distribution?


# Sampling Distribution
Imagine computing the evaluation metric many times but with different eval samples taken from the true eval distribution.

The distribution of the metric is called the **sampling distribution**.

You typically assume the sample mean (your estimated metric based on N samples) is distributed normally, since it is the mean of many independent samples.

We can call the sample mean 
$$
\bar{X} = \frac{X_1 + \cdots + X_n}{N}
$$
Where $N$ is the number of samples, and $X_i$ is the measurement for the ith sample.

# Standard error
The standard error is the standard deviation of the sampling distribution, or equivalently the standard deviation of $\bar{X}$.
$$
\frac{\sigma}{\sqrt{n}}
$$
where $\sigma$ is the standard deviation of each $X_i$.

To reduce the standard error by half, you need to quadruple the number of samples.

# Confidence intrevals
For a Gaussian, 95% of the probaiblity mass sits within 1.96 standard deviations of the mean.

That means that if you run the experiment 100 times, 95% of of the time, the sample mean will fall within 1.96 standard deviations of the true mean.

We can also build a confidence interval around $\bar{X}$, saying the true mean is 
$$
\bar{X} \pm 1.96 \frac{\sigma}{\sqrt{n}}
$$

## Interpretation
The true mean $\mu$ is fixed - it is not random. The confidence interval is random, since it's built from a random sample. There is a 95% probability that your random confidence interval contains the true mean.

## How many samples to you need?

We have $\epsilon = 1.96 \frac{\sigma}{\sqrt{n}}$, so equivalently
$$
n = \left(1.96 \frac{\sigma}{\epsilon} \right)^2
$$


# Wilson
One thing to note is that the sample standard deviation is used to approximate true standard deviation.

In some cases we can run into problems with this. For instance, suppose we are trying to estimate the mean accuracy $p$ of a system. The sample accuracy is a Bernoulli random variable. The standard error is
$$
\sqrt{\frac{Var(X)}{n}} = \sqrt{\frac{(1-\hat{p})\hat{p}}{n}} 
$$

If our estimate $\hat{p}$ is close to 1, (which is possible if the system is already quite accurate), then the variance gets very low. Also, the confidence interval goes over 1.

Wilson's tests asks "which values of $p$ could have plausibly produced the observation?", and uses these values of $p$ as the confidence interval. A candidate for $p$ is plausible if the observed $\hat{p}$ sits within 1.96 standard deviations of $p$, **where the standard deviation is computed from $p$, not the estimate $\hat{p}$**.

$$
|\hat{p} - p| \leq 1.96 \sqrt{\frac{p(1-p)}{n}}
$$

We can solve this using the quadratic formula to find the center and endpoints of the confidence interval:


$$
\text{center} = \frac{\hat{p} + \frac{z^2}{2n}}{1 + \frac{z^2}{n}}
$$
$$
\text{half-width} = \frac{z}{1 + \frac{z^2}{n}} \sqrt{\frac{\hat{p}(1-\hat{p})}{n} + \frac{z^2}{4n^2}}
$$

This is an asymmetric interval, and the center is not $\hat{p}$, but actually pulled toward $\frac{1}{2}$.


Last Reviewed: 08/17/2026
