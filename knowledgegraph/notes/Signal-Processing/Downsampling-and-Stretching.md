# Downsampling
## Time Domain
Downsampling by a factor of M takes every Mth data point.

$$
\text{Downsample}_M(x) = x[Mn]
$$


## DFT Domain
$$
\text{Downsample}_M(x) \leftrightarrow \frac{1}{M}\text{Alias}_M(X)
$$
$$
\text{Alias}_{M,\omega}(X) = \sum_{k=0}^{M-1} X\left(\omega + k \frac{2\pi}{M}\right)
$$

You can also remember it from the perspective of discrete frequency. Remember that the number of DFT points is equal to the number of data points in the time domain. This means downsampling by a factor of N decreases the number of DFT points by the same factor. To account for this decrease, you can think of the DFT spectrum as folded in on itself or overlapping. This is called **aliasing**.

# Stretching
## Time Domain
Stretching by a factor of $L$ inserts $L-1$ zeros between each datapoint.

$$
\text{Stretch}_L(x) = x\left[\frac{n}{L}\right], n = 0 \text{ mod } L
$$

## DFT Domain
- Stretching replicates the FFT spectrum over and over again.
- If we look at just the positive frequencies, it looks like stretching essentially takes the spectrum and mirrors it across the old Nyquist frequency.

Last Reviewed: 8/21/2026