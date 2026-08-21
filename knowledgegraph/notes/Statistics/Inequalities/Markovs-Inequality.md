- The probability of being big cannot be too big.
    - (without the average going up)
- The mean must be a certain mount
    - (if the probability of being big is something).

Assume $X$ is a non-negative random variable. Suppose we have some threshold $t$.


# Derivation

By the law of total expectation:
$$
E[X] = E[X | X < t] P(X < t) + E[X | X \geq t] P(X \geq t)
$$
Now we will show that there are lower bounds for the first and the second terms.

The first term  $E[X | X < t] P(X < t) \geq 0$
$$
E[X] \geq E[X | X \geq t] P(X \geq t)
$$

$E[X | X \geq t] \geq t$
$$
E[X] \geq t  P(X \geq t)
$$
Therefore 
$$
\boxed{
P(X \geq t) \leq \frac{E[X]}{t} 
}
$$


# Intuition
## Visual
- $t$ splits the probabiity distribution into two halves, and $P(X<t) and P(X\geq t)$ tells us the mass on both halves.
- You can picture shifting all the probability mass between those two halves at will, and figuring out how low you can make the expectation. If you shift all the mass to the left, then you will get an expectation of $tP(X\geq t)$.
## Intuitive
- If the probability that $X$ is greater than $t$ is too high, then it ends up raising the expectation, even if the average for $X < t$ is zero.
- Not too many people can be above average, otherwise the average is actually higher.

# Notes
- Note that in the proof, there is a lower bound for both expectations, $0$ and $t$. There is a higher bound of $t$ for the first expectation, but no higher bound for the second one

# Examples
## Example 1
If 50% of the people make over $100,000 a year, then the average income must be at least $50,000. This is quite intuitive, but in terms of markov's inequality, it means
$$E[X] \geq t P(X \geq t)$$
$$E[X] \geq 100,000 * 0.5$$

## Example 1
If the average income is $50,000, then there can be at most 50% of people making $100,000 a year.

$$
P(X \geq t) \leq \frac{E[X]}{t}
$$
$$
P(X \geq 100,000) \leq \frac{50,000}{100,000}
$$

# Source
https://www.youtube.com/watch?v=e-nAr3MkAII

Last reviewed: 08/17/2026