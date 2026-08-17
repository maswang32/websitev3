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

# Questions
Why is it called the evidence?



Last Reviewed 8/16/2026
