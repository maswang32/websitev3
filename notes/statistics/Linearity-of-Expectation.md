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


## Example 1
How many fixed points are there when you do a random permutation of $n$ items?





### Answer
The number of fixed points is

$$
E[1_1 + \cdots 1_n] = E[1_1] + \cdots + E[1_n]
$$
where $1_i$ is the indicator variable for if the item at position $i$ remained unchanged.

$E[1_i]$ = $\frac{1}{n}$, since for any given item, there is a  $\frac{1}{n}$ chance that it stayed.

Therefore the answer is $n * \frac{1}{n} = 1$.


## Example 2 (Coupon Collector)
Suppose each cereal box comes with one of $n$ different possible toys. How many cereal boxes would you expect to buy before seeing all the toys?

### Answer
Let $T$ be the number of boxes it takes to see all $n$ toys.

Let $t_i$ be the number of boxes it takes to see a new toy after $i - 1$ toys have already been seen.

Then the time it takes to see all the toys can be segmented up into the amount of time it takes to see each new toy:
$$
T = t_1 + \cdots + t_n
$$

Taking the expectation and using linearity:
$$
E[T] = E[t_1 + \cdots + t_n] = E[t_1] + \cdots + E[t_n]
$$

Now $E[t_1]$ = 1, since you will always see a new toy if you haven't seen any already. 

Otherwise, the probabilty of seeing a new toy when you get a new box is $\frac{n-(i-1)}{n}$ if you have already seen $i-1$ toys.

Since it it a geometric random variable with $p = \frac{n-(i-1)}{n}$, and the expectation is $\frac{1}{p}$, this means the expected number of boxes before seeing a new toy is $\frac{n}{n-(i-1)}$.

Thus, our expectation is

$$
= 1 + \frac{n}{n-1} + \frac{n}{n-2} + \cdots + \frac{n}{2} + \frac{n}{1}
$$
Or
$$
n \left(\frac{1}{1} + \frac{1}{2} + \cdots + \frac{1}{n-2} + \frac{1}{n-1} + \frac{1}{n}\right)
$$

Or $n \cdot H_n$, where $H_n = \sum_{k=1}^{n} \frac{1}{k}$ is the $n$th harmonic number.

Last Reviewed: 8/16/2026
