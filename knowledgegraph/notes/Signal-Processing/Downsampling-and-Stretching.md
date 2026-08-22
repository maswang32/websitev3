Remember that the number of DFT points is equal to the number of data points in the time domain. This means downsampling by a factor of N decreases the number of DFT points by the same factor, and stretching increases it by the same factor.

# Downsampling
## Time Domain
- Downsampling takes every $N$th data point.

## DFT Domain
- Downsampling 'folds' the DFT spectrum on itself, which is called **aliasing**

# Stretching
## Time Domain
- Stretching inserts zeros between each datapoint.

## DFT Domain
- Stretching replicates the FFT spectrum over and over again.
- If we look at just the positive frequencies, it looks like stretching essentially takes the spectrum and mirrors it across the old Nyquist frequency.

Last Reviewed: 8/21/2026
