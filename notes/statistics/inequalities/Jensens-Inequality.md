# Jensens Inequality


## Visual Explanation
Imagine a bunch of datapoints $X$, and consider $y = \log(X)$.

We can visualize the $(x, y)$ pairs here. All of them lie along the $y = \log(x)$ curve.

Now take the average of their $x$ coordinates and their $y$ coordinates.

This midpoint is at:
$$
(E[X], E[\log[X]])
$$
Which is below the curve. That is because averaging the y-coordinates will not get you super high, since the logarithmic curve flattens out as $x$ gets larger. But averaging the $x$ coordinates will get you farther to the right.

This point lies below
$$
(E[X], log[E[X]])
$$
Which is actually on the curve.

## From definition of concavity
Supposing $f$ is a concave function, then by definition
$$
f((1-a)x + ay) \geq (1-a)f(x) + af(y)
$$
In other words, the taking a linear combination on the input side is greater than taking a linear combination on the output side.

When we compute expectations, we are essentially taking linear combinations.

Last Reviewed: 08/17/26
