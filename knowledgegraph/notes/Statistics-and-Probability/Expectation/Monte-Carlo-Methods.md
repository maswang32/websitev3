A Monte Carlo estimate simply uses samples from a distribution to estimate an expectation:

$$
\mathbb{E}_{\mathbf{x} \sim p(\mathbf{x})}\left[f[\mathbf{x}]\right] = \int f[\mathbf{x}] p(\mathbf{x}) d\mathbf{x} \approx \frac{1}{N} \sum^N_{n=1} f[\mathbf{x}_n]
$$


Last Reviewed 10/3/2026
