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


Note that the expectation of an indicator variable for an event is the same as the probability that the event occurs. Thus, $E[1_A] = P(A)$, and the above expression is just the sum of the probabilities.


## Example
How many fixed points are there when you do a random permutation of $n$ items?

### Answer
The number of fixed points is

$$
E[1_1 + \cdots 1_n] = E[1_1] + \cdots + E[1_n]
$$
where $1_i$ is the indicator variable for if the item at position $i$ remained unchanged.

$E[1_i]$ = $\frac{1}{n}$, since for any given item, there is a  $\frac{1}{n}$ chance that it moved.

Therefore the answer is $n * \frac{1}{n} = 1$.

Last Reviewed: 8/16/2026
