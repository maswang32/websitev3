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

# Interpretation
The true mean $\mu$ is fixed - it is not random. The confidence interval is random, since it's built from a random sample. The p-value is the probability that your random confidence interval contains the true mean.

# p-value
Probability of seeing the data (or more extreme) given the null hypothesis

# Permutation Test
If you randomly shuffle data and labels, what are the odds you get data this extreme or greater?

# Type 1 and Type 2 Errors
- Type 1 Error: False positive - you reject the null when it is actually true. We call the probability of a type 1 error $\alpha$. 
- Type 2 Error: False negative - we accept the null hypothesis when the null hypothesis is false. We call the probability of a Type 2 error to be $\beta$.

# Statistical Power
This is 1 - $\beta$.





Last Reviewed: 08/17/2026
