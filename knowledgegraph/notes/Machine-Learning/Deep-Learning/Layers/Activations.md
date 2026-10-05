# Gated Activations
$$
\text{GLU} = (\mathbf{A}\mathbf{x} + \mathbf{b})\odot\sigma(\mathbf{C}\mathbf{x} + \mathbf{d})
$$
$$
\text{SwiGLU} = (\mathbf{A}\mathbf{x} + \mathbf{b})\odot\text{Swish}(\mathbf{C}\mathbf{x} + \mathbf{d})
$$


# Pocketed Activation
## Dead ReLU problem
Imagine zooming into a single ReLU in the neural network. During the forward pass, we can imagine each data example 'hitting' a different part of this ReLU.

The dead ReLU problem occurs when the pre-activations (before the ReLU is applied) become more and more negative, and further and further away from zero.

If no examples in a batch have positive preactivations, gradient during the backward pass does not flow backward through the ReLU.

It is likely to remain dead, since the weights feeding into that preactivation will not be updated either.

## Pocketed Activations
To solve this issue, there are pocketed activations, like GeLU, Swish and Mish.

These pocketed activations have a global minimum near zero. 

Focusing on a specific example during the backward pass. 

If the upstream gradient says the post-activation value needs to decrease:
1. In a ReLU, the gradient on the pre-activation will push to to become negative.
2. In a pocketed activation, the gradient on the pre-activation will push it **closer** to the global minimum, regardless of where the pre-activation is right now.

Thus, instead of the preactivations becoming super negative, they typically get stuck in the pocket near zero. 

Enough examples can potentially remove them from the pocket. Suppose we have a batch of examples and the upstream gradient says the post-activation value needs to increase. For some examples (those to the right of the global minimum), this means increasing the preactivation value, and for others (those to the left of the global minimum), this means decreasing the preactivation value. Usually the slope on the right side of the pocket is higher, so ot's possible these effects can push the preactivation out of the pocket. 

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
