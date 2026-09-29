Bayes' Law:
$$
P(A|B) = \frac{P(B|A)P(A)}{P(B)}
$$


# Metaphorically: 

$$
P(\text{Hypothesis} | \text{Data}) = \frac{P(\text{Data} | \text{Hypothesis})P(\text{Hypothesis})}{P(\text{Data})}
$$

## Naming the variables
On the right hand side:

- $P(\text{Hypothesis})$ is called the **prior** - your probability of the hypothesis, before observing any data.
- $P(\text{Data} | \text{Hypothesis} )$ is called the **likelihood**, since this is the probability your model (hypothesis) assigns to the data
- $P(Data)$ is called the **evidence**, or the probability of observing the data, marginalized over all hypotheses.

On the left hand side, $P(\text{Hypothesis} | \text{Data})$ is called the **posterior**, or the probability of the hypothesis after observing the data.


## Analysis
- If the **prior** belief in the hypothesis is high, then the **posterior** is higher.
- If the **likelihood** (probability of the data given the hypothesis) is high, then our **posterior** (updated belief in our hypothesis) is high
- If the probability of the **data** we observed is low, then the **posterior** is higher


# Disease Question
Suppose a disease hits 1% of people, the test catches 90% of sick people, and has false alarms on 9% of healthy people.

If you test positive, what are the chances you have the disease?

## Answer
Expressing the question in terms of math:
$$
P(D) = 0.01, P(T|D) = 0.9, P(T|D^c) = 0.09
$$
And we want $P(D|T)$.
Writing Bayes':
$$
P(D|T) = \frac{P(T|D)P(D)}{P(T)}
$$
$$
= \frac{P(T|D)P(D)}{P(T \cap D) + P(T \cap D^c)}
$$
$$
= \frac{P(T|D)P(D)}{P(T|D)P(D) + P(T|D^c)P(D^c)}
$$
$$
= \frac{0.9\times 0.01}{0.9 \times 0.01 + 0.09 \times 0.99}
$$
$$
= 0.092
$$
Intuitively, if you imagine you have a thousand people, 99% of them do not have the disease, and 9% of those will test positive.

1% of them do have the disease, and 90% of them will test positive.

Of the people that test positive, most of them will not have the disease, since 9% of 99% is much larger than 90% of 1%.

# Bayesian Update

Notice that to get from the prior $P(H)$ to the posterior $P(H|D)$, you multiply by $\frac{P(D|H)}{P(D)}$.


# Odds and Likelihood Ratio
Odds are "how many times more likely is $H_1$ than $H_2$?

You can compute this via Bayes:

$$
P(H_1 | D) = \frac{P(D | H_1)P(H_1)}{P(D)}
$$
$$
P(H_2 | D) = \frac{P(D | H_2)P(H_2)}{P(D)}
$$
$$
\frac{P(H_1 | D)}{P(H_2 | D)} = \frac{P(H_1)}{P(H_2)} \times \frac{P(D | H_1)}{P(D | H_2)}
$$

The term on the left is the "posterior odds". The term in the middle called "prior odds". The term on the right is the "likelihood ratio".

You can take your prior odds and multiply by the likelihood ratio to get the posterior, or take the log of all three terms, which makes the likelihood ratio additive.

# Questions
Why is it called the evidence?


Last Reviewed 8/16/2026
