Linearity of Expectation:
$$
E[X + Y] = E[X] + E[Y]
$$

This is true even if $X$ and $Y$ are not independent.


# Practical Use
Many statistical questions ask for "the expected number" of times an event occurs in $n$ trials, which may or may not be independent.

If we define a random variable $X$ to be the number of times an event occursm then we have:

$$
X = 1_1 + \cdots + 1_n
$$
$$
E[X] = E[1_1 + \cdots + 1_n]
$$
By linearity of expectation, this i 
$$
E[1_1] + \cdots + E[1_n]
$$
Again, this is true even if the trials are not independent.

Last Reviewed: 8/16/2026
