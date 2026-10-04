# Gated Activations
$$
\text{GLU} = (\mathbf{A}\mathbf{x} + \mathbf{b})\cdot\sigma(\mathbf{C}\mathbf{x} + \mathbf{D})
$$
$$
\text{SwiGLU} = (Ax + b)*\text{Swish}(Cx + D)
$$


# Pocketed Activation
## Dead ReLU problem
The dead ReLU problem occurs when the pre-activation (before the ReLU is applied) gets negative, and far from zero. 

Gradient does not flow backward through a ReLU that is dead. If no training examples can activate it, it is likely to remain dead, since the weights feeding into that preactivation will not be updated either.

## Pocketed Activations
To solve this issue, there are pocketed activations, like GeLU, Swish and Mish.

If the preactivation is very negative, there is still a gradient.

Instead of the preactivation becoming super negative, they typically get stuck in the pocket near zero, which is a local minima.

Enough examples can potentially remove from pocket by pushing the preactivation one way or the other.

## GeLU
GeLU is like setting the dropout probabilty to the CDF of the neuron value, and taking the expectation
$$
\text{GeLU}(\mathbf{x}) = x \Phi(\mathbf{x})
$$
Where $\Phi(\mathbf(x))$ is the standard Gaussian CDF function.


# Observations on Activations
SwiGLU has a squared part, where its derivative vanishes near zero.

The ReLU squared activation also does this

The Snake activation also does this - it has a $x^2$ term in its expansion

Last Reviewed: 1/17/25
