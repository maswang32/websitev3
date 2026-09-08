# Confusion Matrix:
- Rows = what machine learning algorithm predicted
- Columns = known truth

|                    | Actually Positive | Actually Negative |
| --------------------| -------------------| -------------------|
| Predicted Positive | TP                | FP                |
| Predicted Negative | FN                | TN                |

- False Negatives = "Not actually negative, algorithm says it is"
- False Positives = "Not actually positive, algorithm says it is"
- On-diagonal = Correct
- Off-diagonal = incorrect
- To compare two models on the same dataset, you can compare them across the two numbers on the diagonal (TP and TN counts)
    - Or, you can compare them on the two numbers off the diagonal (FP and FN rate)
    - These two numbers can disagree though.

# Precision and Recall
## Precision
- Labeled positive and is positive / Number of examples you labeled as positives
- True positives / (True positives + False positives)
- TP / (TP + FP)

## Recall
- Labeled positive and is positive / Number of positives 
- TP / P
- TP / (TP + FN)
- Also called "Sensitivity"

## Specificity
- What percentage of negatives were correctly identified as negative?
- Recall of the negative class
- TN / N
- TN / (TN + FP)

## Analogy
Imagine you have some gold pellets in a bunch of dirt pellets. The gold pellets are the positive examples, and the dirt pellets are the negative examples.

You take a scoop out of the gold and dirt mixture.

Precision is the proportion of stuff in your scoop that is gold.

Recall/Sensitivity is how much of the total gold you got.

Specificity is the proportion of the dirt pellets you managed to ignore.

## Decisions
Choose the one with the better recall if capturing positives is more important
Choose the one with better specificity if capturing negatives is more important

## Generalization to multi-category
You can calculate precision, recall/sensitivity, and specificity for each category.

In this case consider positives to be in the category, and negatives to be not in category.



# Threshold
- Your model gives you a score, you can threshold this score to determine if something gets classified as positive or negative.
- Each threshold gives you a (precision, recall) pair.



# F1 Score
- Harmonic mean of precision and recall.
    - Harmonic so that a terrible value kills the score
    - Arithmetic means that 50% is always guaranteed.


## Averaging
- Micro-averaging - average per example
- Macro-averaging - average per language