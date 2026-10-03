# Gated Activations
$$
\text{GLU} = (\mathbf{A}\mathbf{x} + \mathbf{b})\cdot\sigma(\mathbf{C}\mathbf{x} + \mathbf{D})
$$
$$
\text{SwiGLU} = (Ax + b)*\text{Swish}(Cx + D)
$$



# Observations on Activations
SwiGLU has a squared part, where its derivative vanishes near zero.

The ReLU squared activation also does this

The Snake activation also does this - it has a $x^2$ term in its expansion

Last Reviewed: 1/17/25
