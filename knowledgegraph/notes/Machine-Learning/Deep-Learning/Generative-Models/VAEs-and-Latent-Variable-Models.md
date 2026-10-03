# 1. Overview
- As generative models do, VAEs aim to model the probability distribution $p(\mathbf{x})$, where $\mathbf{x}$ is the random variable representing the data.

- VAEs cannot actually evaluate the probability density $p(\mathbf{x})$ for a given sample $\mathbf{x}$ directly. However, VAEs do
allow you to sample from $p(\mathbf{x})$.

- In Maximum likelihood Estimation, we would directly attempt to maximize the likelihood of our observed data under our model of the probability distribution.

- In VAEs, we instead maximize a lower bound for the likelihood, called the ELBO.




# 2. Latent Variable Models
Model a joint distribution $p(\mathbf{x}, \mathbf{z})$, and express $p(\mathbf{x})$ as:
$$
\int p(\mathbf{x}, \mathbf{z}) d \mathbf{z}
$$
This joint distribution is typically modeled as this product:
$$
p(\mathbf{x}, \mathbf{z}) = p(\mathbf{x} | \mathbf{z}) p(\mathbf{z})
$$
This breakdown lets you model complex distributions with relatively simple ones.

## a. Example: Mixture of Gaussians
You can write a mixture of Gaussians this way, for instance the latent variable $\mathbf{z}$ could be discrete, and tell you which Gaussian you are sampling from, and $p(\mathbf{x} | \mathbf{z})$ would be a different Gaussian based on the value of $\mathbf{z}$.

We can compute $p(\mathbf{x})$ directly by marginalizing (summing) over $\mathbf{z}$.

## b. VAEs/Continuous Latent Variable Models
We will set up the VAE as a latent variable model.
1. The prior is the standard normal distribution:
$$p(\mathbf{z}) = N_{\mathbf{z}}(\mathbf{0}, \mathbf{I})$$
2. The likelihood is is a normal distribution, whose mean is approximated by a neural network $\mathbf{f}$, which is the decoder of the VAE. The distribution has a spherical covariance of $\sigma^2 \mathbf{I}$.
$$
p_{\phi}(\mathbf{x} | \mathbf{z}) = N_{\mathbf{x}}(\mathbf{f}_{\phi}\left[\mathbf{z} \right], \sigma^2\mathbf{I})
$$
3. We also define another distribution:
$$q_{\phi}(\mathbf{z} | \mathbf{x}) = N_z ( \mathbf{g}_{\phi}(\mathbf{x})_{\mu}, \mathbf{g}_{\phi}(\mathbf{x})_{\Sigma})$$
This distribution is another normal distribution whose mean and variance are approximated by a neural network $\mathbf{g}$, called the encoder. 

The data likelihood under the parameters $\phi$ is:
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

Note that the encoder does not determine the model's likelihood of the data. We will soon see that it does determine the evidence lower bound (ELBO), which is a lower bound on the likelihood, that approaches the likelihood as $q_{\theta}(\mathbf{z} | \mathbf{x})$ approximates $p_{\phi} (\mathbf{z} | \mathbf{x})$.


## c. Generation via Ancestral Sampling
You can generate samples by sampling $\mathbf{z}$, then sampling from $p(\mathbf{x} | \mathbf{z})$.

For instance, in a continuous latent variable model, we would sample $\mathbf{z} \sim N_{\mathbf{z}}[\mathbf{0}, \mathbf{I}]$ then pass $\mathbf{z}$ through the decoder, then sample from the distribution outputted by the decoder.


# 3. Evidence Lower Bound (ELBO)
## Intractability of MLE
The goal is to maximize the probability of the observed training data:
$$
\sum_{i=1}^N \log \left[ p_{\phi}(\mathbf{x}_i) \right]
$$
Our expression for $p_{\phi}(\mathbf{x})$ is 
$$
\int p_{\phi}(\mathbf{x} , \mathbf{z}) d\mathbf{z}
=
\int p_{\phi}(\mathbf{x} | \mathbf{z}) p(\mathbf{z}) d\mathbf{z}
=
\int N_{\mathbf{x}}\left[ \mathbf{f}[\mathbf{z}, \phi], \sigma^2 \mathbf{I} \right] \cdot N_{\mathbf{z}} [\mathbf{0}, \mathbf{I}] d\mathbf{z}
$$
But computing this integral is intractable. 

## ELBO Derivation
Instead, we will maximize a lower bound on the log-likelihood, called the evidence lower bound or ELBO.
1. Instead of simply modeling $p$ with parameters $\phi$, we will also model another probability distribution $q$ with parameters $\theta$. 
2. Both of these will contribute to our expression for the evidence lower bound, although only $p_{\phi}$ contributes to our expression of the likelihood.
3. $\phi$ will eventually become the parameters of our decoder, and $\theta$ will eventually be the parameters for our encoder.

$$
\log \left[ p_{\phi}(\mathbf{x}) \right] = \log \left[\int p_{\phi}(\mathbf{x}, \mathbf{z}) d\mathbf{z} \right]
$$

Let $q_{\theta}(\mathbf{z} | \mathbf{x})$ be a distribution over $\mathbf{z}$.
$$
 = \log \left[\int q_{\theta}(\mathbf{z} | \mathbf{x})\frac{p_{\phi}(\mathbf{x},\mathbf{z})}{q_{\theta}(\mathbf{z} | \mathbf{x})} d\mathbf{z} \right]
$$
By Jensen's inequality, we get that this is greater than or equal to:
$$
 \geq \int q_{\theta}(\mathbf{z} | \mathbf{x}) \log \left[ \frac{p_{\phi}(\mathbf{x},\mathbf{z})}{q_{\theta}(\mathbf{z} | \mathbf{x})} \right] d\mathbf{z}
$$
This expression is called the evidence lower bound, since $p_{\phi}(\mathbf{x})$ is called the evidence in Bayes' rule.

## ELBO Intuition
When we are trying to maximize ELBO, we either make the lower bound tighter, or make the actual log likelihood higher, or both. Thus, maximizing ELBO can be a good way to maximize likelihood.

To visualize ELBO:
1. The log-likelihood of the data is a function of the parameters $\phi$.
2. Similarly, the ELBO is also a function of the parameters $\phi$, for any fixed $\theta$. 
3. This function of $\phi$ must lie below the log likelihood for all values of $\phi$.
4. When we change $\theta,$ we modify the ELBO function, which changes the lower bound.
5. When we change $\phi$, we are moving along the lower bound function.

![ELBO Diagram](ELBO-Diagram.png)


## ELBO as Log Likelihood minus KL Divergence
$$
\text{ELBO}[\phi, \theta] =  \int q_{\theta}(\mathbf{z} | \mathbf{x}) \log \left[ \frac{p_{\phi}(\mathbf{x},\mathbf{z})}{q_{\theta}(\mathbf{z} | \mathbf{x})} \right] d\mathbf{z}
$$
Factoring out $p_{\phi}(\mathbf{x})$:
$$
= \int q_{\theta}(\mathbf{z} | \mathbf{x}) \log \left[ \frac{p_{\phi}(\mathbf{z} | \mathbf{x}) p_{\phi}(\mathbf{x})}{q_{\theta}(\mathbf{z} | \mathbf{x})} \right] d\mathbf{z}
$$
$$
= \int q_{\theta}(\mathbf{z} | \mathbf{x}) \left( \log\left[p_{\phi}(\mathbf{x}) \right] + \log \left[ \frac{p_{\phi}(\mathbf{z} | \mathbf{x}) }{q_{\theta}(\mathbf{z} | \mathbf{x})} \right] \right) d\mathbf{z}
$$
$$
= \int q_{\theta}(\mathbf{z} | \mathbf{x})  \log\left[p_{\phi}(\mathbf{x}) \right]d\mathbf{z} + \int q_{\theta}(\mathbf{z} | \mathbf{x}) \log \left[ \frac{p_{\phi}(\mathbf{z} | \mathbf{x}) }{q_{\theta}(\mathbf{z} | \mathbf{x})} \right] d\mathbf{z}
$$
$$
= \log\left[p_{\phi}(\mathbf{x}) \right] + \int q_{\theta}(\mathbf{z} | \mathbf{x}) \log \left[ \frac{p_{\phi}(\mathbf{z} | \mathbf{x}) }{q_{\theta}(\mathbf{z} | \mathbf{x})} \right] d\mathbf{z}
$$
$$
= \log\left[p_{\phi}(\mathbf{x}) \right] - \int q_{\theta}(\mathbf{z} | \mathbf{x}) \log \left[ \frac{q_{\theta}(\mathbf{z} | \mathbf{x})}{p_{\phi}(\mathbf{z} | \mathbf{x}) } \right] d\mathbf{z}
$$
$$
= \log\left[p_{\phi}(\mathbf{x}) \right] - \mathbb{E}_{\mathbf{z} \sim q_{\theta}(\mathbf{z} | \mathbf{x})} \left[ \log \left[ \frac{q_{\theta}(\mathbf{z} | \mathbf{x})}{p_{\phi}(\mathbf{z} | \mathbf{x}) } \right] \right]
$$
$$
= \log\left[p_{\phi}(\mathbf{x}) \right] - D_{\text{KL}}\left(q_{\theta}(\mathbf{z} | \mathbf{x}) \parallel p_{\phi}(\mathbf{z} | \mathbf{x}) \right)
$$

### Interpretation
From this derivation, the ELBO is equal to the original log likelihood minus the KL divergence between $q_{\theta}(\mathbf{z} | \mathbf{x})$ and $p_{\phi}(\mathbf{z} | \mathbf{x})$. 

Recall that $p_{\phi}$ corresponds to the decoder, and $q_{\theta}$ corresponds to the encoder. The decoder (and prior) imply some distribution of $\mathbf{z}$ given $\mathbf{x}$, which is called $p_{\phi}(\mathbf{z} | \mathbf{x})$. The encoder will directly compute $q_{\theta}(\mathbf{z} | \mathbf{x})$.

Thus, this KL is **the difference between the distribution implied by the decoder and the distribution computed by the encoder for $\mathbf{z}$ given $\mathbf{x}$**.

Since $p_{\phi}(\mathbf{z} | \mathbf{x})$  is not actually tractable to compute, the encoder's job is to approximate it with $q_{\theta}(\mathbf{z} | \mathbf{x})$.
The tightness of the bound (how close ELBO is to the likelihood) is determined by how well the encoder estimates the true posterior implied by the decoder.
If it approximates it perfectly, then the ELBO is equal to the likelihood.


#### Why is the posterior $p_{\phi} (\mathbf{z} | \mathbf{x})$ intractable to compute? 
If we write it using Bayes' rule, we get
$$
p_{\phi}(\mathbf{z} | \mathbf{x}) = \frac{p_{\phi}(\mathbf{x} | \mathbf{z}) p(\mathbf{z})}{p_{\phi}(\mathbf{x})}
$$
And the evidence term $p_{\phi}(\mathbf{x})$ is not possible to compute, as stated before.

#### Notes on the Encoder
Recall that we chose a simple parametric form for $q_{\theta}(\mathbf{z} | \mathbf{x})$, which is a Gaussian with mean and covariance given by a neural network $\mathbf{g}$.

This parametric form will have some error with the posterior implied by the decoder, but it is what we do to make it expressible by a neural network.


## ELBO is Reconstruction Loss Minus Prior KL
$$
\text{ELBO}[\phi, \theta] =  \int q_{\theta}(\mathbf{z} | \mathbf{x}) \log \left[ \frac{p_{\phi}(\mathbf{x},\mathbf{z})}{q_{\theta}(\mathbf{z} | \mathbf{x})} \right] d\mathbf{z}
$$
Factoring out $p(\mathbf{z})$:
$$
= \int q_{\theta}(\mathbf{z} | \mathbf{x}) \log \left[ \frac{p_{\phi}(\mathbf{x} | \mathbf{z}) p(\mathbf{z})}{q_{\theta}(\mathbf{z} | \mathbf{x})} \right] d\mathbf{z}
$$
$$
= \int q_{\theta}(\mathbf{z} | \mathbf{x}) \log \left[ p_{\phi}(\mathbf{x} | \mathbf{z} ) \right] d \mathbf{z} + \int q_{\theta}(\mathbf{z} | \mathbf{x}) \log \left[ \frac{p(\mathbf{z})}{q_{\theta}(\mathbf{z} | \mathbf{x})} \right] d\mathbf{z}
$$
$$
= \mathbb{E}_{\mathbf{z} \sim q_{\theta}(\mathbf{z} | \mathbf{x})} \left[   \log \left[ p_{\phi}(\mathbf{x} | \mathbf{z} ) \right] \right]+ \mathbb{E}_{\mathbf{z} \sim q_{\theta}(\mathbf{z} | \mathbf{x})} \left[ \log \left[ \frac{p(\mathbf{z})}{q_{\theta}(\mathbf{z} | \mathbf{x})} \right] \right]
$$
$$
= \mathbb{E}_{\mathbf{z} \sim q_{\theta}(\mathbf{z} | \mathbf{x})} \left[   \log \left[ p_{\phi}(\mathbf{x} | \mathbf{z} ) \right] \right] - \mathbb{E}_{\mathbf{z} \sim q_{\theta}(\mathbf{z} | \mathbf{x})} \left[ \log \left[ \frac{q_{\theta}(\mathbf{z} | \mathbf{x})}{p(\mathbf{z})} \right] \right]
$$
$$
= \mathbb{E}_{\mathbf{z} \sim q_{\theta}(\mathbf{z} | \mathbf{x})} \left[   \log \left[ p_{\phi}(\mathbf{x} | \mathbf{z} ) \right] \right] - D_{\text{KL}}\left(q_{\theta}(\mathbf{z} | \mathbf{x}) \parallel p(\mathbf{z}) \right)
$$
Note that in a VAE, the prior $p(\mathbf{z})$ is typically a normal distribution with unit covariance, and has no parameters.

### Interpretation
In other words, you can view the ELBO (which we want to maximize) as a reconstruction term minus the divergence of $q_{\theta}(\mathbf{z} | \mathbf{x})$ from the prior $p(\mathbf{z})$.

The reconstruction term is intractable to compute directly, but can be approximated by sampling.

CONTINUE FROM AFTER FIGURE 17.8

# Questions
- What is the final model for $p(\mathbf{x})$?
- Figure 17.7 caption
- What does the KL divergence mean
