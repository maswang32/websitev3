# Sources of Error
Test error is a cause of these things:

## Noise
**Uncertainty in the task**
From a probabilitistic perspective, the best thing that the model can do is predict the true conditional distribution of the outputs given the inputs. There will still be error even if this distribution is modeled perfectly, since the inputs may not contain all the information needed to perfectly predict the outputs.

- For instance,
    - Measurement noise can be seen as a factor unpredictable from the input.
    - Other explanatory variables are not observed
    - The task has multiple possible outputs for each input
- All of these are kind of the same case, the input contains incomplete information.
- Independent of the model - related to the task (which is predicting a set of outputs from a set of inputs)
- Noise is usually but not always present (e.g. modeling a complicated deterministic function)
- Fitting the training data perfectly may still be possible, since we are unlikely to see the exact same training input twice.

## Bias
**Model is not flexible enough**
- The model may be restricted and cannot fit the true function - e.g., MLP fitting a piecewise linear function to a sinusoid.

## Variance
**Training Data is not enough**
The training data is a *sample* from the true training distribution - resulting in different models depending on the sampled training data.

- Improved by adding more data.
- variance also exists in the optimization process.


## Mathematical Noise-Bias-Variance Decomposition (MSE Loss)
Suppose we are doing a 1D regression task where we are trying to predict $y$ from $x$.

Let us consider $x$ to be inputs from the test distribution that we care about.

Consider $p(y | x)$ to be the true conditional distribution of outputs given inputs.

Let $\mu[x]$ to be a function providing the mean of the conditional distibution 

Let $f(x,\phi)$ be a function in our model family, parametrized by $\theta$.

### Loss for a specific input/output pair
Let us write down the expression for the MSE Loss for a given input/output pair. The ground truth label $y[x]$ is sampled from $p(y | x)$.
$$
L[x] = (f[x, \phi] - y[x])^2
$$
$$
= \left(f[x, \phi] - \mu[x] + \mu[x] - y[x]\right)^2
$$
$$
= \left( (f[x, \phi] - \mu[x]) + (\mu[x] - y[x])\right)^2
$$
$$
= (f[x, \phi] - \mu[x])^2 + 2 (f[x, \phi] - \mu[x])(\mu[x] - y[x]) + (\mu[x] - y[x])^2
$$

### Expected Loss for a given input
Above, we computed loss for a specific input/output pair.

Since $y[x]$ is sampled from $p(y|x)$, there are many possible ground-truth output labels given the input $x$. 

We can compute the expected loss for a given input $x$ by marginalizing over $y$.

$$
E_y\left[(f[x, \phi] - \mu[x])^2 + 2 (f[x, \phi] - \mu[x])(\mu[x] - y[x]) + (\mu[x] - y[x])^2\right]
$$
$$
E_y\left[(f[x, \phi] - \mu[x])^2\right] + 2 E_y\left[(f[x, \phi] - \mu[x])(\mu[x] - y[x])\right] + E_y\left[(\mu[x] - y[x])^2\right]
$$
$$
(f[x, \phi] - \mu[x])^2 + 2 (f[x, \phi] - \mu[x])E_y\left[(\mu[x] - y[x])\right] + (\mu[x] - y[x])^2
$$
By definition of $\mu[x]$ to be the mean of the conditional distribution, we hvae that the middle term goes to zero:
$$
(f[x, \phi] - \mu[x])^2 + 2 (f[x, \phi] - \mu[x])\cdot 0 + (\mu[x] - y[x])^2
$$
$$
\boxed{E_y\left[L[x]\right] = (f[x, \phi] - \mu[x])^2 + (\mu[x] - y[x])^2}
$$
The first term is the bias and variance combined: how much does the model deviate from the true conditional distribution? The second term is the noise term, which is the error expected from modeling the true conditional distribution. You will notice that is proportional to the variance in the true conditional distribution.

### Decomposing the Bias and Variance
Observe that the parameters $\phi$ of our model $f$ are a function of the training data, which we denote as $D$. Let $f[x,\phi[D]]$ be the model output when we train on the dataset $D$, which is a sample of the true data distribution.

Now let $f_\mu[x] = E_D\left[f\left[x, \phi[D]\right]\right]$ be the expectation of $f$ over all possible datasets $D$.

Now we can do the same trick again, adding and subtracing $f_\mu[x]$:

$$
E_y\left[L[x]\right] = (f[x, \phi[D]] - \mu[x])^2 + (\mu[x] - y[x])^2
$$
$$
= (f[x, \phi[D]] - f_\mu[x] + f_\mu[x] - \mu[x])^2 + (\mu[x] - y[x])^2
$$
$$
= (f[x, \phi[D]] - f_\mu[x])^2 + 2(f[x, \phi[D]] - f_\mu[x])(f_\mu[x] - \mu[x]) + (f_\mu[x] - \mu[x])^2 + (\mu[x] - y[x])^2
$$

Now lets take the expectation over all possible training datasets $D$:

$$
E_D\left[E_y\left[L[x]\right]\right] = E_D\left[(f[x, \phi[D]] - f_\mu[x])^2 + 2(f[x, \phi[D]] - f_\mu[x])(f_\mu[x] - \mu[x]) + (f_\mu[x] - \mu[x])^2 + (\mu[x] - y[x])^2\right]
$$

$$
E_D\left[E_y\left[L[x]\right]\right] = E_D\left[(f[x, \phi[D]] - f_\mu[x])^2\right] + 2\left(E_D\left[f[x, \phi[D]]\right] - f_\mu[x]\right)(f_\mu[x] - \mu[x]) + (f_\mu[x] - \mu[x])^2 + (\mu[x] - y[x])^2
$$

Now, since $E_D\left[f[x, \phi[D]]\right] =  f_\mu[x]$ by definition, the cross term goes to zero, and we get

$$
\boxed{
E_D\left[E_y\left[L[x]\right]\right] = E_D\left[(f[x, \phi[D]] - f_\mu[x])^2\right] + (f_\mu[x] - \mu[x])^2 + (\mu[x] - y[x])^2}
$$
Given a data example, we have computed the expected loss with respect to different possible outputs and training datasets. We have decomposed this error into three terms: The first term is the variance, the second term is the bias, and the third term is the noise.


## Intuitive Explanation on how each error goes to zero
1. For noise to go to zero, the outputs must determine the inputs (the conditional distribution of outputs given inputs is a point mass.)
2. For variance to go to zero, we must train on the entire data distribution.
3. For bias to go to zero, the model must be able to fit the true function exactly.

## Bias-Variance Tradeoff
- How does the model fill in the blanks for limited training data? This is bias and variance.
- Increasing model capacity decreases bias, since the model can fit the training data better, but this often increases variance
- For a fixed dataset, there is often an optimal model size.

## Overfitting
- Extra model capacity fits the noise term instead of just reducing bias
- For instance, imagine modeling a noisy sinusoid with a piecewise linear segments. If you model with fewer linear segments, the noise in the observations will cancel out over each segment. But if you increase the number of segments, there are fewer observations in each.

# What if test Loss Increases, but test Error stays the same?
- Test loss increases due to the model being more confidently incorrect. As the model continues training, it drives logits to more extreme values to try to maximize the probability of the training data. This also results in the model being more confidently incorrect about wrong answers, and increases the negative log likelihood (the loss) of the correct answer.
- Test error can remain the same in this regime.


Last Reviewed: 08/21/2026
