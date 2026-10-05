# Multiplication in time is convolution in frequency

Think of representing your signal as a sum of complex sinusoids of diffferent frequencies:

$$
x[n] = X_1w_1 + \cdots + X_nw_n 
$$

This is a polynomial, whose coefficients are the Fourier coefficients, or the frequency domain representation of the signal.

When you multiply two polynomials:

$$
x[n] y[n] = (X_1w_1 + \cdots + X_nw_n) (Y_1w_1 + \cdots + Y_nw_n)
$$

You are essentially convolving the coefficients. For instance, the coefficient on $w_k$ will be a sum of the products $X_iY_j$ such that $i + j = k$.

Thus, multiplication in the time domain can be seen as multiplying two polynomials, whose coefficients are the Fourier coefficients of the two signals. When we multiply the polynomials, we convolve their coefficients, which amounts to convolving the Fourier representation of the two signals.

Thus, multiplication in the time domain is convolution in the frequency domain.

Last Reviewed: 10/3/2026
