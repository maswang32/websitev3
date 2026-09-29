Break a hard expectation into cases.

$$
E[X] = E[E[X|Y]]
$$

On the right hand side, the outer expectation is integrated over $y$, and the inner one is integrated over $x$.

In other words, compute the expectation of $X$ given every possible $Y$. Then weight these by the probabilities of each of the $Y$s.


# Example
A coin has probability $p$ of landing heads. What is the expected number of times we need to flip to get the first heads?

## Answer

Let $Y$ be 1 if the first flip was heads, 0 if not.

Break it up into two cases: 

$$
E[X] = P(Y=1) * E[X|Y=1] + P(Y=0) * E[X|Y=0]
$$
$$
E[X] = P(Y=1) * 1 + P(Y=0) * (1 + E[X])
$$
$$
E[X] = p * 1 + (1-p) * (1 + E[X])
$$
$$
E[X] = p + (1 - p + E[X] - pE[X])
$$
$$
pE[X] = 1
$$
$$
\boxed{E[X] = 1/p}
$$

Last Reviewed 08/16/2026
