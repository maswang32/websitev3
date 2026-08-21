
# p-value
Probability of seeing the data (or more extreme) given the null hypothesis.

NOT these two things, which invert the conditioning:
1. The probability of the null hypothesis
2. The probabliity the results are due to chance

$p$ is typically thresholded by $\alpha$, which is set to be 0.05 by convention.

$\alpha$ is set by us, $p$ is determined by the experiment.

# Permutation Test
If you randomly shuffle data and labels, what are the odds you get data this extreme or greater?

# Type 1 and Type 2 Errors
- Type 1 Error: False positive - you reject the null when it is actually true. We call the probability of a type 1 error $\alpha$. 
- Type 2 Error: False negative - we accept the null hypothesis when the null hypothesis is false. We call the probability of a Type 2 error to be $\beta$.

# Statistical Power
This is 1 - $\beta$.


# Bonferroni
If $\alpha=0.05$, that still means one out of every 20 experiments could show significance even if the null hypothesis is true. We have to adjust the threshold $\alpha$ by dividing it by the number of trials.


Last Reviewed 08/17/26