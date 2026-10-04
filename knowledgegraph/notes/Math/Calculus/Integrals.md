# Integrals as Limits

Suppose we have a rectangular approximation to a definite integral with limits $a$ and $b$.

We take $N$ evenly spaced points $x_1, \ldots, x_N$, where $x_1 = a$ and $x_N = b$. This corresponds to $N-1$ rectangles. The area under the curve is approximated as:

$$
\sum_{i=1}^{N - 1} f(x_i) (x_{i+1} - x_{i}) =
\sum_{i=1}^{N - 1} f(x_i) \Delta x
$$

Where $\Delta x$ is $x_{i+1} - x_{i}$. 

As we take $\Delta x \rightarrow 0^+$:

$$
\sum_{i=1}^{N - 1} f(x_i) \Delta x \rightarrow \int_a^b f(x) dx
$$

Note that $dx$ replaces $\delta x$, and the integral replaces the summation. The $dx$ represents an infinitely small change in $x$.


## Example
$$
\int_a^b dx = b - a
$$
Since we are essentially adding a bunch of slices $dx$ up that sum to $b - a$:
$$
\lim_{\Delta x \rightarrow 0} \left[ \sum_{i=1}^{N - 1} f(x_i) \Delta x \right]
= \lim_{\Delta x \rightarrow 0} \left[ \sum_{i=1}^{N - 1} \Delta x \right]
= \lim_{\Delta x \rightarrow 0} \left[ b - a \right] =  b - a
$$

Last Reviewed: 10/3/2026
