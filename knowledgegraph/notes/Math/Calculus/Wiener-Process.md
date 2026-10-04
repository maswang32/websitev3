# Standard Wiener Process
## Intuition
A Wiener process (also called Brownian motion) is a continuous time process that is like a random walk. 

Imagine a discrete-time random process where you start at position $\mathbf{x}_{t=0} = \mathbf{0}$. Then, your position at time $t$ is determined by

$$
\mathbf{x}_{t + \Delta t} = \mathbf{x}_{t} + \mathcal{N}(\mathbf{0},\Delta t \mathbf{I})
$$

Or equivalently,

$$
\mathbf{x}_{t + \Delta t} = \mathbf{x}_{t} + \sqrt{\Delta t} \cdot \mathcal{N}(
\mathbf{0}, \mathbf{I})
$$

In other words, every timestep, you change your position by a vector sampled from $\mathcal{N}(\mathbf{0},\Delta t \mathbf{I})$, where $\Delta t$ is how long the timestep is.

A Wiener process is the continuous limit of this as $\Delta t \rightarrow 0$.

## Definition
We define a collection of random variables indexed by time, which we can think of as a function mapping the time $t$ to a random variable. It satisfies the property that
$$
W_0 = \mathbf{0}
$$

And, for any $t_2 > t_1$:

$$
W_{t_2} - W_{t_1} \sim \mathcal{N}(\mathbf{0}, (t_2 - t_1)\mathbf{I})
$$

### Independence
1. $W_{t_2} - W_{t_1}$ is independent from $W_{s}$, $s < t_1$.
2. The change in any time interval is independent from the change at any non-overlapping time interval.

### Variance
Recall that the variance of the sum of two independent random variables is the sum of the variances. Since the change in non-overlapping time intervals is independent, and we can think of the position at time $t$ as the sum of tiny, incremental changes in non-overlapping intervals, the variance accumulates over time.

### Marginalization
$$
W_{t} \sim \mathcal{N}(\mathbf{0}, t\mathbf{I})
$$

### Infinitesimal Version
We can think of the Wiener process like this: At every time step, we take an infinitesimally small step in a random direction proportional to a vector sampled from the standard normal:
$$
dW \sim \mathcal{N}(\mathbf{0}, \mathbf{I} dt)
$$

Last Reviewed: 10/3/2026
 