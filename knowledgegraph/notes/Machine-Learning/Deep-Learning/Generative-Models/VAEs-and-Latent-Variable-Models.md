# Overview
- VAEs aim to model the probability distribution $p(\mathbf{x})$ over the random variable representing the data, which is $\mathbf{x}$.

- VAEs allow you to sample from $p(\mathbf{x})$, but cannot evaluate the probability density for given data samples.

- Maximum likelihood estimation is not possible - therefore, VAEs maximize a lower bound on the likelihood.**

# Latent Variable Models
Model a joint distribution $p(\mathbf{x}, \mathbf{z})$, and express $p(\mathbf{x})$ as:
$$
\int p(\mathbf{x}, \mathbf{z}) d \mathbf{z}
$$
This joint distribution is typically modeled as this product:
$$
p(\mathbf{x}, \mathbf{z}) = p(\mathbf{x} | \mathbf{z}) p(\mathbf{z})
$$
This breakdown lets you model complex distributions. 

## Example 1 - Mixture of Gaussians
You can write a mixture of gaussians this way, for instance the latent variable $\mathbf{z}$ could be discrete, and tell you which Gaussian you are sampling from, and $p(\mathbf{x} | \mathbf{z})$ would be a different Gaussian based on the value of $\mathbf{z}$.

We can compute $p(\mathbf{x})$ directly by marginalizing (summing) over $\mathbf{z}$.

## Example 2 - Latent Variable Model
$p(\mathbf{z})$ could be the standard normal distribution, and $p_{\phi}(\mathbf{x} | \mathbf{z})$ could be approximated by the decoder of a VAE, with mean $\mathbf{f}[\mathbf{z}, \phi]$ and spherical covariance $\sigma^2 \mathbf{I}$.


The data probability is
$$
p_{\phi}(\mathbf{x}) = \int p_{\phi}(\mathbf{x}, \mathbf{z}) d\mathbf{z}
$$
$$
 = \int p_{\phi}(\mathbf{x} | \mathbf{z}) p(\mathbf{z}) d\mathbf{z}
$$
$$
 = \int N_{\mathbf{x}}\left[ \mathbf{f}[\mathbf{z}, \phi], \sigma^2 \mathbf{I} \right] \cdot N_{\mathbf{z}} [\mathbf{0}, \mathbf{I}] d\mathbf{z}
$$

Which is a weighted sum of Gaussians of different means, where the means are the decoder outputs $\mathbf{f}[\mathbf{z}, \phi]$ where $\mathbf{z} \sim p(\mathbf{z})$, and the weight on each Gaussian is $p(\mathbf{z})$.

### Ancestral Sampling
You can generate samples by sampling $\mathbf{z} \sim N_{\mathbf{z}}[\mathbf{0}, \mathbf{I}]$ then passing it through the decoder, then sampling from the distribution outputted by the decoder.


# Training
The goal is to maximize the probability of the observed training data:
$$
\sum_{i=1}^N \log \left[ p_{\phi}(\mathbf{x}_i) \right]
$$
Our expression for $p_{\phi}(\mathbf{x})$ is 
$$ \int N_{\mathbf{x}}\left[ \mathbf{f}[\mathbf{z}, \phi], \sigma^2 \mathbf{I} \right] \cdot N_{\mathbf{z}} [\mathbf{0}, \mathbf{I}] d\mathbf{z}
$$
But computing this integral is intractable. Instead, we will maximize a lower bound on the log-likelihood, called the evidence lower bound or ELBO.

$$
\log(p_{\phi}(\mathbf{x})) = \log \left(\int p_{\phi}(\mathbf{x}, \mathbf{z}) d\mathbf{z} \right)
$$

Let $q(\mathbf{z})$ be a distribution over $\mathbf{z}$.
$$
 = \log \left(\int q(\mathbf{z})\frac{p_{\phi}(\mathbf{x},\mathbf{z})}{q(\mathbf{z})} d\mathbf{z} \right)
$$
By Jensen's inequality, we get that this is greater than or equal to:
$$
 \geq \int q(\mathbf{z}) \log \left[ \frac{p_{\phi}(\mathbf{x},\mathbf{z})}{q(\mathbf{z})} \right] d\mathbf{z}
$$
This expression is called the evidence lower bound, since $p_{\phi}(\mathbf{x})$ is called the evidence in Bayes' rule.





# Questions
What is the final model for $p(\mathbf{x})$?