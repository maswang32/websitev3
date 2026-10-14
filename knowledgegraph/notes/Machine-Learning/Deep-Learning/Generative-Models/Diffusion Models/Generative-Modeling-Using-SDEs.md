# 1. Forward-Time Diffusion

For a noise-conditional score network, there is a finite number of noise levels.

As the number of diffusion timesteps approaches infinity ($L \rightarrow \infty$), the noise level becomes a continuous-time stochastic process, where noise is added continuously.


We have:

$$
d\mathbf{x} = \mathbf{f}(\mathbf{x}, t) dt + g(t)d\mathbf{w}
$$

- $d\mathbf{w}$ can be viewed as infinitesimal white noise, and characterizes a [Wiener Process](Wiener-Process.md).

- $\mathbf{f}$ is a vector-valued function representing the *drift coefficient* and $g(t)$ is a scalar-valued function called the *diffusion coefficient*.
  - The drift coefficient determines how $\mathbf{x}$ evolves over time deterministically
  - Observe that the diffusion term is stochastic, but the coefficient $g$ does not depend on $\mathbf{x}$. It does depend on $t$, however.

We can imagine applying this diffusion process to our data. As $t$ changes, the distribution of our data changes. We can use $p_t(\mathbf{x})$ to denote the probability distribution of our data at diffusion time $t$, where $t \in [0,T]$. The data distribution (with no diffusion) is $p_0(\mathbf{x})$.

In addition, we can let $\mathbf{X}_t$ be a random variable representing the value of a datapoint at diffusion time $t$, and use $\mathbf{x}_t$ to represent a realization of $\mathbf{X}_t$.

We choose our diffusion process so that $p_T$ does not depend on $p_0$. Typically this is something like pure Gaussian noise. This allows easy initialization of the reverse diffusion process, which goes from $t=T$ to $t=0$.

### Additional Thoughts
- In DDPMs, the *drift coefficient* $\mathbf{f}(\mathbf{x}, t)$ would be analogous to $\sqrt{1-\beta_t}$ when defining the forward process. In the SDE model, the drift coefficient tells you the deterministic part of $\mathbf{x}$'s change over time. In DDPMs, this deterministic part is the $\mathbf{x}_0$ component, which diminishes over time as we add more and more noise. Thus, the drift coefficient is kind of like the time-derivative of the coefficient on $\mathbf{x}_0$ in DDPMs.
- In DDPMs, the diffusion coefficient is analogous to $\sqrt{\beta_t}$. It is kind of like the time-derivative of $\sigma_i$ or the time-derivative of the coefficient on the noise term in DDPMs. $g^2(t)$ is the rate at which noise variance is added.

## Choices of $\mathbf{f}(\mathbf{x},t), g(t)$

We can choose the diffusion and drift coefficients as hyperparameters. For instance, we can choose a forward diffusion process:

$$
d\mathbf{x} = e^t d\mathbf{w}
$$
Which means that the variance grows exponentially as time increases, and is similar to choosing a geometric progression of noise scales $\sigma_1, \ldots, \sigma_L$. This is an example of a  **variance exploding** SDE. The Variance Exploding SDE, the Variance Preserving SDE, and the sub-VP SDE work well for generating images.

# 2. Reverse-Time Diffusion

The reverse diffusion process is defined as:

$$
d\mathbf{x} = \left[\mathbf{f}(\mathbf{x},t) - g^2(t)\nabla_\mathbf{x} \log(p_t(\mathbf{x}))\right] dt + g(t)d\mathbf{\bar{w}}
$$

If we know the drift and diffusion coefficients (which are from the forward process), and can approximate the score function (the gradient of the data distributions at time $t$), then we can compute the reverse-time SDE.

We can sample from any marginal distribution $p_t$ (determined by the forward process) by sampling from $p_T$ (which should be doable, since this should approximate an easy-to-sample-from distribution), then by integrating from $T$ to $t$. By integrating all the way to $t=0$, we should be able to generate a data sample.

### Additional Thoughts
- Note that $dt$ represents an infinitesimal *negative* time step, since we are integrating from higher $t$ to lower $t$.
- $\mathbf{\bar{w}}$ is described as 'reverse-time Brownian motion'. In practice, $d\mathbf{\bar{w}}$ is Gaussian noise, just like $d\mathbf{w}$ in the forward process.




# 3. Learning the Score Function
## a - Ideal Optimization Objective
We would like to fit the score function such that

$$
\mathbf{s}_\theta(\mathbf{x}, t) \approx \nabla_\mathbf{x} \log p_{t} (\mathbf{x})
$$

Thus, we minimize the distance between these two functions, across a continuous weighted sum:

$$
\mathbb{E}_{t \sim \mathcal{U}(0,T)}
\mathbb{E}_{\mathbf{x} \sim p_t(\mathbf{x})}
\left[
\lambda(t)
\lVert
\nabla_\mathbf{x} \log p_{t} (\mathbf{x}) -
\mathbf{s}_\theta(\mathbf{x}, t)  \rVert^2_2
\right]
$$

Where $\lambda(t)$ is a weighting function. 

We can use denoising score matching to optimize this objective.

In addition, we use the exponential moving average of the weights during sampling.

### Notes on the weighting function
We would like to balance the losses across different values of $t$. One way to do this is to adjust by the magnitude of the target we are fitting to, which in practice is the score estimate conditioned on $\mathbf{x}_0$, or $\nabla_{\mathbf{x}_t} \log p_t(\mathbf{x}_t | \mathbf{x}_0)$. Thus, we select:

$$
\lambda(t) \propto 1/
\mathbb{E}_{p_t(\mathbf{x})} \left[
\lVert
\nabla_{\mathbf{x}_t}
\log p_{t} (\mathbf{x}_t \mid \mathbf{x}_0) \rVert^2_2 \right]
$$
Often, these weights are proportional to $\sigma^2$, just like they were in NCSNs.

To implement this weighting, we rescale the outputs of the network, so its outputs are on the same scale across time-steps.


### Additional Thoughts
- The weights are proportional to the amount of noise added: Recall in our NCSN notes that smaller noise levels have larger score magnitudes. The expectation in the denominator is actually inversely proportional to the variance of the noise added.
- Note that in DDPM, the network is always predicting samples from $\mathcal{N}(\mathbf{0}, \mathbf{I})$ no matter the timestep, which is similar to rescaling the outputs of the network in score-based models.



## b - Equivalent Optimization Objective, using the Conditional Score
We have

$$
\mathbb{E}_{t \sim \mathcal{U}(0,T)}
\mathbb{E}_{\mathbf{x} \sim p_t(\mathbf{x})}
\left[
\lambda(t)
\lVert
\nabla_\mathbf{x} \log p_t (\mathbf{x}) -
\mathbf{s}_\theta(\mathbf{x}, t)  \rVert^2_2
\right]
$$

We can estimate this objective as 

$$
\mathbb{E}_{t \sim \mathcal{U}(0,T)}
\lambda(t)
\left[
\mathbb{E}_{\mathbf{x}_0 \sim p_0(\mathbf{x})}
\mathbb{E}_{\mathbf{x}_t \sim p_t(\mathbf{x}_t \mid \mathbf{x}_0)}
\left[
\lVert
\nabla_\mathbf{x} \log p_{t} (\mathbf{x}_t \mid \mathbf{x}_0) -
\mathbf{s}_\theta(\mathbf{x}_t, t)  \rVert^2_2
\right]
\right]
$$

### Additional Thoughts
- We would like the score function to fit $\nabla_{\mathbf{x}_t} \log p_{t} (\mathbf{x}_t)$, but this distribution may be complex and multimodal. However, $\log p_{t} (\mathbf{x}_t \mid \mathbf{x}_0)$ is just Gaussian.

- Since the score function we are fitting does not see $\mathbf{x}_0$, it will fit an expectation over all possible $\mathbf{x}_0$, which will approximate the score function of $p_t(\mathbf{x}_t)$.
- The probability distribution of $p_t(\mathbf{x}_t)$ is a mixture of Gaussians, which means that the conditional distribution $\log p_{t} (\mathbf{x}_t \mid \mathbf{x}_0)$ locally approximates $\log p_{t} (\mathbf{x}_t)$ at the point $\mathbf{x}_t$, at least at low noise levels where the Gaussians do not overlap too much.

## c - Equivalence between Ideal Optimization Objective and Conditional-Score Objective.
Our intended objective is:

$$
\mathbb{E}_{t \sim \mathcal{U}(0,T)}
\mathbb{E}_{\mathbf{x} \sim p_t(\mathbf{x})}
\left[
\lambda(t)
\lVert
\nabla_\mathbf{x} \log p_t (\mathbf{x}) -
\mathbf{s}_\theta(\mathbf{x}, t)  \rVert^2_2
\right]
$$

We would like to show this objective is equivalent:

$$
\mathbb{E}_{t \sim \mathcal{U}(0,T)}
\lambda(t)
\left[
\mathbb{E}_{\mathbf{x}_0 \sim p_0(\mathbf{x})}
\mathbb{E}_{\mathbf{x}_t \sim p_t(\mathbf{x}_t \mid \mathbf{x}_0)}
\left[
\lVert
\nabla_\mathbf{x} \log p_{t} (\mathbf{x}_t \mid \mathbf{x}_0) -
\mathbf{s}_\theta(\mathbf{x}_t, t)  \rVert^2_2
\right]
\right]
$$


### I. Lemma - Express Marginal Distribution as an expectation of the conditional 

We first show that we can estimate the marginal distribution as an expectation of the conditionals:

$$
\nabla_{\mathbf{x}_t} \log p_t(\mathbf{x}_t) = \mathbb{E}_{\mathbf{x}_0\sim p_t(\mathbf{x}_0 \mid \mathbf{x}_t)} \left[
    \nabla_{\mathbf{x}_t} \log p_t(\mathbf{x}_t \mid \mathbf{x}_0)
\right]
$$

In other words, we can approximate the marginal score function by sampling from the posterior, and aggregating the score estimates that we can compute from single samples.

#### Additional Note: Proof of Lemma

$$
p_t(\mathbf{x}_t) = \int p_t(\mathbf{x}_t | \mathbf{x}_0) p_0(\mathbf{x}_0) d\mathbf{x}_0
$$
$$
\nabla_{\mathbf{x}_t} \log p_t(\mathbf{x}_t) = \frac{\nabla_{\mathbf{x}_t} p_t(\mathbf{x}_t)}{p_t(\mathbf{x}_t)}
$$
Which comes from the chain rule.

Substituting the RHS of the first equation into the RHS of the second,
$$
\nabla_{\mathbf{x}_t} \log p_t(\mathbf{x}_t) = \frac{\nabla_{\mathbf{x}_t} \left[ \int p_t(\mathbf{x}_t | \mathbf{x}_0) p_0(\mathbf{x}_0) d\mathbf{x}_0 \right]}{p_t(\mathbf{x}_t)}
$$
The gradient can be moved inside the integral, and only applies to the one term depending on $\mathbf{x}_t$:
$$
= \frac{ \int \nabla_{\mathbf{x}_t} \left[ p_t(\mathbf{x}_t | \mathbf{x}_0) \right] p_0(\mathbf{x}_0) d\mathbf{x}_0 }{p_t(\mathbf{x}_t)}
$$
Note that 
$$
\nabla_{\mathbf{x}_t} \log p_t(\mathbf{x}_t  | \mathbf{x}_0) = \frac{\nabla_{\mathbf{x}_t} p_t(\mathbf{x}_t  | \mathbf{x}_0)}{p_t(\mathbf{x}_t  | \mathbf{x}_0 )} \Rightarrow \nabla_{\mathbf{x}_t} p_t(\mathbf{x}_t  | \mathbf{x}_0) = \nabla_{\mathbf{x}_t} \log p_t(\mathbf{x}_t  | \mathbf{x}_0) p_t(\mathbf{x}_t  | \mathbf{x}_0)
$$
Substituting the expression for $\nabla_{\mathbf{x}_t} p_t(\mathbf{x}_t  | \mathbf{x}_0)$ in:
$$
\nabla_{\mathbf{x}_t} \log p_t(\mathbf{x}_t) = \frac{ \int \left[ \nabla_{\mathbf{x}_t} \log p_t(\mathbf{x}_t  | \mathbf{x}_0) p_t(\mathbf{x}_t  | \mathbf{x}_0) \right] p_0(\mathbf{x}_0) d\mathbf{x}_0 }{p_t(\mathbf{x}_t)}
$$
$$
= \int \frac{  \nabla_{\mathbf{x}_t} \log p_t(\mathbf{x}_t  | \mathbf{x}_0) p_t(\mathbf{x}_t  | \mathbf{x}_0) p_0(\mathbf{x}_0) }{p_t(\mathbf{x}_t)}d\mathbf{x}_0 
$$
Using Bayes' Rule:
$$
= \int  \nabla_{\mathbf{x}_t} \log p_t(\mathbf{x}_t  | \mathbf{x}_0) p_t(\mathbf{x}_0  | \mathbf{x}_t) d\mathbf{x}_0 
$$
$$
= \mathbb{E}_{\mathbf{x}_0 \sim p_t(\mathbf{x}_0 | \mathbf{x}_t)} \left[\nabla_{\mathbf{x}_t} \log p_t(\mathbf{x}_t  | \mathbf{x}_0)  \right]
$$


### II. Bias Variance Decomposition
By the bias-variance decomposition, we have:

$$
\mathbb{E} \| Z - a \|^2_2 =  \| \mathbb{E}[Z] - a \|^2_2 + \mathbb{E} \left[ \| Z - \mathbb{E}[Z] \|^2_2 \right] \\[10pt]
= \| \mathbb{E}[Z] - a \|^2_2 + \operatorname{Var}(Z)
$$

For any random variable $Z$.

### III. Applying Bias-Variance Decomposition and the Lemma to show the two objectives are equal given $\mathbf{x}_t$
Consider the new expression

$$
\tag{*}
\mathbb{E}_{\mathbf{x}_0\sim p_t(\mathbf{x}_0 \mid \mathbf{x}_t)} \left[
\left\lVert
    \nabla_{\mathbf{x}_t} \log p_t(\mathbf{x}_t \mid \mathbf{x}_0) - \mathbf{s}_\theta(\mathbf{x}_t, t) \right\rVert^2_2 \right]
$$

By the bias-variance decomposition, this is equal to

$$
\left\lVert
\mathbb{E}_{\mathbf{x}_0\sim p_t(\mathbf{x}_0 \mid \mathbf{x}_t)} \left[
    \nabla_{\mathbf{x}_t} \log p_t(\mathbf{x}_t \mid \mathbf{x}_0)
\right] - \mathbf{s}_\theta(\mathbf{x}_t, t) \right\rVert^2_2 +
\operatorname{Var}\left[\nabla_{\mathbf{x}_t} \log p_t(\mathbf{x}_t \mid \mathbf{x}_0)\right] = \\[10pt]
\left\lVert
\mathbb{E}_{\mathbf{x}_0\sim p_t(\mathbf{x}_0 \mid \mathbf{x}_t)} \left[
    \nabla_{\mathbf{x}_t} \log p_t(\mathbf{x}_t \mid \mathbf{x}_0)
\right] - \mathbf{s}_\theta(\mathbf{x}_t, t) \right\rVert^2_2 + C
$$

Where we use $C$ to denote the variance expression, which is constant given the forward process and does not depend on model parameters $\theta$. By the Lemma, this is equal to

$$
\tag{**}
\left\lVert
\nabla_{\mathbf{x}_t} \log p_t(\mathbf{x}_t) - \mathbf{s}_\theta(\mathbf{x}_t, t) \right\rVert^2_2 + C 
$$

Which is our score matching objective for a single timestep, plus a constant.

### IV. Wrapping in expectation
Let us wrap both starred expressions (which we have proven to be equal) in an expectation over $\mathbf{x}_t$:

$$
\mathbb{E}_{\mathbf{x}_t\sim p_t(\mathbf{x}_t)}
\mathbb{E}_{\mathbf{x}_0\sim p_t(\mathbf{x}_0 \mid \mathbf{x}_t)} \left[
\left\lVert
    \nabla_{\mathbf{x}_t} \log p_t(\mathbf{x}_t \mid \mathbf{x}_0) - \mathbf{s}_\theta(\mathbf{x}_t, t) \right\rVert^2_2 \right] = \\[10pt]
\mathbb{E}_{\mathbf{x}_t\sim p_t(\mathbf{x}_t)}\left[
\left\lVert
\nabla_{\mathbf{x}_t} \log p_t(\mathbf{x}_t) - \mathbf{s}_\theta(\mathbf{x}_t, t) \right\rVert^2_2 + C \right]
$$

We can change how we express the order of the two expectations on the RHS:
$$
\mathbb{E}_{\mathbf{x}_0\sim p_0(\mathbf{x}_0)}
\mathbb{E}_{\mathbf{x}_t\sim p_t(\mathbf{x}_t \mid \mathbf{x}_0)}
\left[
\left\lVert
    \nabla_{\mathbf{x}_t} \log p_t(\mathbf{x}_t \mid \mathbf{x}_0) - \mathbf{s}_\theta(\mathbf{x}_t, t) \right\rVert^2_2 \right] = \\[10pt]
\mathbb{E}_{\mathbf{x}_t\sim p_t(\mathbf{x}_t)}\left[
\left\lVert
\nabla_{\mathbf{x}_t} \log p_t(\mathbf{x}_t) - \mathbf{s}_\theta(\mathbf{x}_t, t) \right\rVert^2_2 + C \right]
$$

If we wrap both in another expectation over $t$, and multiply by $\lambda(t)$, we get

$$
\mathbb{E}_{t \sim \mathcal{U}(0,T)}
\lambda(t)
\left[
\mathbb{E}_{\mathbf{x}_0\sim p_0(\mathbf{x}_0)}
\mathbb{E}_{\mathbf{x}_t\sim p_t(\mathbf{x}_t \mid \mathbf{x}_0)}
\left[
\left\lVert
    \nabla_{\mathbf{x}_t} \log p_t(\mathbf{x}_t \mid \mathbf{x}_0) - \mathbf{s}_\theta(\mathbf{x}_t, t) \right\rVert^2_2 \right]\right] = \\[10pt]
\mathbb{E}_{t \sim \mathcal{U}(0,T)}
\lambda(t)
\left[
\mathbb{E}_{\mathbf{x}_t\sim p_t(\mathbf{x}_t)}\left[
\left\lVert
\nabla_{\mathbf{x}_t} \log p_t(\mathbf{x}_t) - \mathbf{s}_\theta(\mathbf{x}_t, t) \right\rVert^2_2 + C \right] \right]
$$

The $C$ term can be taken out of the inner expectation, and remains constant with respect to $\theta$ when it is taken outside of the outer expectation:

$$
\mathbb{E}_{t \sim \mathcal{U}(0,T)}
\lambda(t)
\left[
\mathbb{E}_{\mathbf{x}_0\sim p_0(\mathbf{x}_0)}
\mathbb{E}_{\mathbf{x}_t\sim p_t(\mathbf{x}_t \mid \mathbf{x}_0)}
\left[
\left\lVert
    \nabla_{\mathbf{x}_t} \log p_t(\mathbf{x}_t \mid \mathbf{x}_0) - \mathbf{s}_\theta(\mathbf{x}_t, t) \right\rVert^2_2 \right]\right] = \\[10pt]
\mathbb{E}_{t \sim \mathcal{U}(0,T)}
\lambda(t)
\left[
\mathbb{E}_{\mathbf{x}_t\sim p_t(\mathbf{x}_t)}\left[
\left\lVert
\nabla_{\mathbf{x}_t} \log p_t(\mathbf{x}_t) - \mathbf{s}_\theta(\mathbf{x}_t, t) \right\rVert^2_2 \right] \right] + C_2
$$

The left hand side is the objective that we train with, and the right hand side is the optimization objective. Thus, we have that the two optimization objectives are equivalent - they differ by a constant that does not depend on our parameters $\theta$.

# 4. Solving the Reverse-Time SDE (Integration/Sampling)

## Reverse Time SDE Integral
To generate samples, we can evaluate the reverse-time SDE. This is as simple as coming up with a numerical approximation to the integral of the reverse-time SDE process:

$$
d\mathbf{x} = \left[\mathbf{f}(\mathbf{x},t) - g^2(t)\nabla_\mathbf{x} \log(p_t(\mathbf{x}))\right] dt + g(t)d\mathbf{\bar{w}}
$$

#### Additional Notes

We can express our SDE in integral form:

$$
\mathbf{x}_t = \mathbf{x}_{t_0} + \int_{t_0}^t \left[\mathbf{f}(\mathbf{x}_s,s) - g^2(s)\nabla_\mathbf{x} \log(p_s(\mathbf{x}_s))\right] ds + \int_{t_0}^t g(s)d\mathbf{\bar{w}}(s)
$$

Where

$$
d\mathbf{\bar{w}}(s) \sim \mathcal{N}(\mathbf{0}, ds\,\mathbf{I})
$$

This results from integrating both sides of the differential equation from $t_0$ to $t$.

Particularly, to get a sample from a marginal distribution, we can evaluate this integral with $t_0 = T$:

$$
\mathbf{x}_t = \mathbf{x}_T + \int_{T}^t \left[\mathbf{f}(\mathbf{x}_s,s) - g^2(s)\nabla_\mathbf{x} \log(p_s(\mathbf{x}_s))\right] ds + \int_{T}^t g(s)d\mathbf{\bar{w}}(s)
$$

Since we can sample $\mathbf{x}_T$ in closed form.

Finally, to generate a sample from the data distribution, we are interested in $\mathbf{x}_0$. This can be obtained by setting $t=0$ in the above equation.

## Numerical Integration
Choose a small $\Delta t < 0$.

Then perform this process:

1. $\mathbf{x}_T \sim \pi$

2. $
\mathbf{x}_{t + \Delta t} = \mathbf{x}_t + \left[ \mathbf{f}(\mathbf{x}_t,t) - g^2(t) \mathbf{s}_\theta(\mathbf{x}_t, t) \right] \Delta t + g(t)\mathbf{z}_t\sqrt{| \Delta t |}
$

Where $\mathbf{z}_t \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$, and $\pi$ approximates $p_T(\mathbf{x}_T)$, and is easy to sample from. 

#### Additional Notes
- Note that the last term on the right side is a way to sample from $\mathcal{N}(\mathbf{0}, g^2(t) | \Delta t | \mathbf{I})$.

- This is similar to Langevin Sampling or "noisy gradient descent" for when time was not continuous.

# 5. ODE Version

We can change the SDE into an ODE without changing its marginal distributions $p_t(\mathbf{x}_t)$. The formula is this:

$$
d\mathbf{x} = \left[\mathbf{f}(\mathbf{x}, t) - \frac{1}{2} g^2(t)\nabla_\mathbf{x} \log p_t(\mathbf{x}) \right] dt
$$

ODE trajectories are actually smoother, and this process is invertible. We can directly convert $\mathbf{x}_0$ to $\mathbf{x}_T$ and convert it back. 

This is a special case of a continuous time neural ODE and a normalizing flow, and allows for exact likelihood computation.



# 6. Connection to DDPM
Once I finish my page on DDPM, you will be able to see that the ELBO objective that DDPM uses is the same as the score-matching objective.

# 7. Extra Stuff
## 'Likelihood' Weighting

If $\lambda(t) = g^2(t)$, we have that

$$
D_{\text{KL}}\left(p_0(\mathbf{x}) \| p_\theta(\mathbf{x})\right) \leq \frac{T}{2} \mathbb{E}_{t \sim \mathcal{U}(0,T)}
\mathbb{E}_{\mathbf{x} \sim p_t(\mathbf{x})}
\left[
\lambda(t)
\lVert
\nabla_\mathbf{x} \log p_t (\mathbf{x}) - 
\mathbf{s}_\theta(\mathbf{x}, t)  \rVert^2_2
\right] + \\ D_{\text{KL}}\left(p_T\left(\mathbf{x}_T\right) \| \pi \left(\mathbf{x}_T\right) \right)
$$

Where $p_\theta(\mathbf{x})$ is the distribution of $\mathbf{x}_0$ we get by running the reverse SDE with our estimated score function, and $\pi$ is a simple distribution that is easy to sample from.


## Predictor-Corrector Methods
The predictor chooses a step size $\Delta t$, then predicts $\mathbf{x}_{t + \Delta t}$ based on $\mathbf{x}_{t}$. Then, we run several 'corrector' steps to improve our sample from $p_{t + \Delta t}$, using our estimate of its score function $\mathbf{s}_\theta(\mathbf{x}_{t + \Delta t}, t + \Delta t)$. We do this before moving on to the next time step.

This is similar to the discrete-time case, where we optimize the score at each noise level before moving to the next noise level.



## Inverse Problems
Suppose we have a known forward process $p(\mathbf{y} \mid \mathbf{x})$, and we would like to know $p(\mathbf{x} \mid \mathbf{y})$.


For instance, $\mathbf{y}$ may be a masked image, and $\mathbf{x}$ can be the full image, unmasked. The known forward process is masking the image. Can we sample from $p(\mathbf{x} | \mathbf{y})$, thus infilling the image's masked regions?

Bayes' rule tells us

$$
p(\mathbf{x} \mid \mathbf{y}) = \frac{p(\mathbf{y} \mid \mathbf{x})p(\mathbf{x})}{p(\mathbf{y})}
$$

By taking the gradient with respect to x of the log of both sides, we get a Bayes' rule for score functions:

$$
\nabla_\mathbf{x} \log p(\mathbf{x} \mid \mathbf{y}) = \nabla_\mathbf{x} \log p(\mathbf{y} \mid \mathbf{x}) + \nabla_\mathbf{x} \log p(\mathbf{x})
$$

Note that the denominator disappears since it does not depend on $\mathbf{x}$. Both terms on the right side of the above expression can be found: the first is given by the known forward process, and the second is the score function of our unconditional distribution (a diffusion model that we have fit to the distribution of images). This will let us sample from $p(\mathbf{x} \mid \mathbf{y})$.

### Additional Note
I am pretty sure $\nabla_\mathbf{x} \log p(\mathbf{y} \mid \mathbf{x})$ is zero everywhere, but I suppose maximizing that will just be ensuring that the non-masked region stays the same.

Last Reviewed: 10/13/2026
