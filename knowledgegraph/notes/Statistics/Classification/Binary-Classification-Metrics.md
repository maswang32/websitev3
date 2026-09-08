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

## Analogy
Imagine you have some gold pellets in a bunch of dirt pellets. The gold pellets are the positive examples, and the dirt pellets are the negative examples.

You take a scoop out of the gold and dirt mixture.

Precision is the proportion of stuff in your scoop that is gold.

Recall is how much of the total gold you got.



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