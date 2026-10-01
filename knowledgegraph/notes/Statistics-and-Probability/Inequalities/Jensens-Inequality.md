# Jensens Inequality
The concave function of an expectation of data is greater than or equal to the expectation of the concave function of the data. Formally, if $f$ is concave, then
$$
f\left(E[X]\right) \geq E[f(X)]
$$



## Visual Explanation
Imagine a bunch of datapoints $X$, and consider $y = \log(X)$.

We can visualize the $(x, y)$ pairs here. All of them lie along the $y = \log(x)$ curve.

Now take the average of their $x$ coordinates and their $y$ coordinates.

This midpoint is at:
$$
(E[X], E[\log[X]])
$$
Which, if you draw it out, is below the curve. 

This point lies below
$$
(E[X], log[E[X]])
$$
Which is actually on the curve.

That is because averaging the y-coordinates will not get you super high, since the logarithmic curve flattens out as $x$ gets larger. But averaging the $x$ coordinates will get you farther to the right.

In other words, the concave function squeezes or saturates the high values, making the expectation after taking the function lower.

## From definition of concavity
Supposing $f$ is a concave function, then by definition
$$
f((1-a)x + ay) \geq (1-a)f(x) + af(y)
$$
In other words, the taking a linear combination on the input side is greater than taking a linear combination on the output side.

When we compute expectations, we are essentially taking linear combinations.

Last Reviewed: 08/17/26
