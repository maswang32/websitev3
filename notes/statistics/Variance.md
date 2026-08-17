Variance is the expected squared difference of a random variable from its mean.
$$
\boxed{Var[X] = E[ (X - E[X])^2]}
$$
# Simplification of formula
$$
Var[X] = E[ (X - E[X])^2]
$$
$$
Var[X] = E[ (X - E[X])(X - E[X])]
$$
$$
Var[X] = E[ (X^2 - 2E[X]X + E[X]^2)]
$$
$$
Var[X] = E[X^2] - E[2E[X]X] + E[E[X]^2]
$$
We can pull the $2E[X]$ out of the middle term since it is a constant, not a random variable.

The last term is also just equal to $E[X]^2$
$$
Var[X] = E[X^2] - 2E[X]E[X] + E[X]^2
$$
$$
\boxed{Var[X] = E[X^2] - E[X]^2}
$$
# Operations with Variance
## Variance of Sum
$$
Var(X+Y) = Var(X) + Var(Y) + 2 Cov(X,Y)
$$
This implies that if $X$ and $Y$ are independent, then
$$
Var(X+Y) = Var(X) + Var(Y)
$$

## Variance of scaled variable
$$
Var(aX) = a^2Var(X)
$$
You can understand this, if $a=2$ then we have $Var(X+X) = Var(X) + Var(X) + 2 Cov(X,X) = Var(X) + Var(X) + 2 Var(X)$

## Variance of mean of random variables
$$
Var(\bar{X}) = Var\left(\frac{X_1 + \cdots + X_N}{N} \right)
$$
$$
 = \frac{1}{N^2} Var\left(X_1 + \cdots + X_N\right)
$$
$$
 = \frac{1}{N^2} N Var(X_1)
$$
$$
\boxed{
= \frac{1}{N} Var(X)
}
$$