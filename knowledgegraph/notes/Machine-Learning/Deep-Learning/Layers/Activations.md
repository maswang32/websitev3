# Gated Activations
$$
\text{GLU} = (\mathbf{A}\mathbf{x} + \mathbf{b})\odot\sigma(\mathbf{C}\mathbf{x} + \mathbf{d})
$$
$$
\text{SwiGLU} = (\mathbf{A}\mathbf{x} + \mathbf{b})\codot\text{Swish}(\mathbf{C}\mathbf{x} + \mathbf{d})
$$


# Pocketed Activation
## Dead ReLU problem
The dead ReLU problem occurs when the pre-activation (before the ReLU is applied) gets negative, and far from zero.

Gradient does not flow backward through a ReLU that is dead. If no training examples can activate it, it is likely to remain dead, since the weights feeding into that preactivation will not be updated either.

## Pocketed Activations
To solve this issue, there are pocketed activations, like GeLU, Swish and Mish.

Instead of the preactivations becoming super negative, they typically get stuck in the pocket near zero, which is a local minimum of the activation function's output.

Neurons that land in the pocket still receive some gradient. Enough examples can potentially remove from pocket by pushing the preactivation one way or the other.

## GeLU
GeLU has a relationship to dropout.
GeLU is like setting the "keep" probability ($1 - p_{dropout}$) to the CDF of the neuron value, and taking the expectation
$$
\text{GeLU}(x) = x \Phi(x)
$$
Where $\Phi(x)$ is the standard Gaussian CDF function.


# Observations on Activations
SwiGLU has a squared part, where its derivative vanishes near zero.

The ReLU squared activation also does this.

The Snake activation also does this - it has an $x^2$ term in its expansion

Last Reviewed: 10/4/2026
