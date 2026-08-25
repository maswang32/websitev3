# Both SigLIP and CLIP
- Dual Encoders, one for vision, one for text
- Each produces a normalized (L2 Norm = 1) embedding
- The temperature is $\tau$
    - Learn the multiplier $t=\frac{1}{\tau}, not the divider.


# CLIP
Loss is:
$$
-\frac{1}{2N} \sum^{N}_{i=1} \left( \log \frac{e^{I_i \cdot T_i/\tau}}{\sum_{j=1}^N e^{I_i \cdot T_j/\tau}}   + \log \frac{e^{I_i \cdot T_i/ \tau} }{\sum_{j=1}^N e^{I_j \cdot T_i/\tau}}\right)
$$

In words:
- We take a batch of $N$ images and $N$ captions.
- We take dot products, scale by a temperature $\tau$, (higher temperature means higher entropy logits)
- We can consider this as a sum of two losses:
    - The first is taking an image as input, and maximizing the probability for the correct text caption
        - In other words, the task is classifying an image input by identifying the correct text caption
        - The bottom sum is over the possible labels, which are different possible text captions
    - The second is taking text as input, and maximizing the probability for the correct image.
- The multipler settles around 100, where it is clamped



# SigLIP
Loss is:
$$
- \frac{1}{N} \sum_{i=1}^N \sum_{j=1}^N \log \frac{1}{1 + e^{-z_{ij}(I_i \cdot T_j / \tau + b)}}
$$

$z_{ij}$ is $1$ if $i=j$, else $-1$

- In contrast to CLIP, we treat each image-text pair independently, like binary classification.
- The bias offsets the positive-negative imbalance - $N$ positives vs $N^2 - N$ negatives.
- The bias is a learned parameter, initialized to -10
    - If bias is 0, sigmoids are around 0.5, loss is large from all the negative pairs.
    - If bias is initialized around -10, sigmoids are around 0
        - loss is small at all the negative pairs, which means we can focus on the positive pairs.
        - The loss for positive pairs is large, since the sigmoids are so close to zero.
- Easier to distribute than CLIP
- Beats CLIP on equal compute.


Last Reviewed: 8/24/2026