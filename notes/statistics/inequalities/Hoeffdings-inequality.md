# Introduction
Suppose we have $X_1,\cdots,X_n$ independent and identically distributed.

Supppose each $X_i$ is a random variable that has a 0.5 chance of being 1, and a 0.5 chance of being -1. Then

$$
E[X_i] = 0
$$

and since all possible values are 1 away from the mean,
$$
Var(X_i) = 1
$$

Now consider
$$
Y = X_1 + \cdots + X_n
$$

$Y$ has a mean of 0, and a variance of $n$. It is approximately normally distributed, or distributed like $N(0, n)$.


## What is the probability that Y is greater than $\sqrt{n}a$?
It is **approximately constant**, since $Y$ is approximately normal

Using the normal CDF,
$$
P\left(\frac{Y}{\sqrt{n}} \geq a\right) \approx 1 - CDF_{N(0,1)}(a)
$$k
In otherwords, the probability mass above $\sqrt{n}a$ is **approximately constant** no matter what $n$ is (it is the probability that the normal distribution is $a$ standard deviations above average).

## What is the probability that Y is greater than $na$?
This probability diminishes. Using Chebyshev,
$$
P(|Y - \mu| \geq na) \leq \frac{Var(Y)}{(na)^2}
$$
$$
P(|Y| \geq na) \leq \frac{Var(Y)}{(na)^2}
$$
$$
P(|Y| \geq na) \leq \frac{n}{(na)^2}
$$
$$
P(|Y| \geq na) \leq \frac{1}{na^2}
$$
By symmetry,
$$
P(Y \geq na) \leq \frac{1}{2na^2}
$$

# Hoeffding's inequality
The probabilty falls exponentially with $n$:
$$
P(X_1 + \cdots + X_n \geq na) \leq e^{-na^2/2}
$$

## Derivation
Fix some $s > 0$, and $a > 0$.

Consider the equivalent event to $Y \geq na$:

$$
e^{s(X_1 + \cdots + X_n)} \geq e^{sna}
$$
Using Markov:
$$
P\left(e^{s(X_1 + \cdots + X_n)} \geq e^{sna} \right) \leq \frac{E[e^{s(X_1 + \cdots + X_n)}]}{e^{sna}}
$$
$$
= 
\frac{E[e^{sX_1} \times \cdots \times  e^{sX_n}]}{e^{sna}}
$$
$$
= 
\frac{E[e^{sX_1}] \times \cdots \times  E[e^{sX_n}]}{e^{sna}}
$$
$$
= 
\frac{\left(E[e^{sX_1}]\right)^n}{e^{sna}}
$$

$$
= 
\left(\frac{E[e^{sX_1}]}{e^{sa}}\right)^n
$$
Now
$$
E[e^{sX_1}] = 0.5e^{-s} + 0.5e^{s}
$$
Making the expression
$$
= 
\left(\frac{0.5(e^{-s} + e^s)}{e^{sa}}\right)^n
$$
Now we want to choose $s$ to make the thing being exponentiated less than one, so that we can achieve a useful upper bound that diminishes as $n$ increases.
### Taylor Series Expansion:
$$
e^x = \sum_{i=0}^{\infty} \frac{x^n}{n!}
$$
$$
0.5(e^{-s} + e^s) = 0.5\left(1 + s + \frac{s^2}{2!} + \frac{s^3}{3!} + \cdots \right) + 0.5\left(1 - s + \frac{s^2}{2!} - \frac{s^3}{3!} + \cdots \right)
$$
All the odd terms cancel, we get:
$$
\left(1 + \frac{s^2}{2!} + \frac{s^4}{4!} + \cdots \right) = \sum_{i=0}^\infty \frac{s^{2i}}{(2i)!}
$$
Now $(2i)! = i! \times (i+1)(i+2)\cdots(2i) \geq i! \times 2^{i} $
So
$$
\sum_{i=0}^\infty \frac{s^{2i}}{(2i)!} \leq \sum_{i=0}^\infty \frac{s^{2i}}{i! \times 2^{i}} =\sum_{i=0}^\infty \frac{ ({s^2/2})^i }{i!} = e^{s^2/2}
$$

Then
$$
\left(\frac{0.5(e^{-s} + e^s)}{e^{sa}}\right)^n \leq \left(\frac{e^{s^2/2} }{e^{sa}}\right)^n  
$$
Lets choose $s = a$ (justification omitted) and get
$$
= \left(\frac{e^{a^2/2} }{e^{a^2}}\right)^n  = (e^{-a^2/2})^n = e^{-na^2/2}
$$
This gives us Hoeffding's inequality:
$$
\boxed{
P(X_1 + \cdots + X_n \geq na) \leq e^{-na^2/2}}
$$

Note that even if $X$ has a different distribution, the derivation would be similar, and we will get a Chernoff bound, which is a more general result.

Last Reviewed: 08/17/2026