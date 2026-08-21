Conditional independence means that two events become unrelated once a third event is known.

# Dropping Variables
Note that if you have conditional independence, you can drop terms. For instance, if events $A$ and $B$ are conditionally independent given $C$, then you have:

$$
P(A | B, C) = P(A | C)
$$

This can be used in derivations, e.g. for DDPMs, you might have 

$$
q(z_2 | z_1, x) = q(z_2 | z_1)
$$
Where $z_1$ is $x$ with added gaussian noise, and $z_2$ is $z_1$ with added gaussian noise.

$x$ provides no additional information when it comes to $z_2$, if we already know $z_1$. So we can drop the condition on $x$.

Last Reviewed: 8/16/2026
