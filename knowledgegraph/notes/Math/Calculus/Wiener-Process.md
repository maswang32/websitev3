# Standard Wiener Process
## Intuition
A Wiener process (also called Brownian motion) is a continuous time process that is like a random walk. 

Imagine a discrete-time random process where you start at position $\mathbf{x_{t=0}} = \mathbf{0}$. Then, your position at time $t$ is determined by

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
We define a set of independent random variables, which we can think of a function mapping the time $t$ to a random variable. It satisfies the property that
$$
W_0 = \mathbf{0}
$$

And 

$$
W_{t_2} - W_{t_1} = \mathcal{N}(0, (t_2 - t_1)I)
$$
Recall that the variance of the sum of two independent random variables is the sum of the variances.

Since the direction you go at any time interval is independent from the direction you go at any non-overlapping time interval, the variance accumulates over linearly over time. We have:
$$
W_{t} = \mathcal{N}(\mathbf{0}, t\mathbf{I})
$$

In other words, at every time step, we take a infinitesimally small step in a random direction proportional to a vector sampled from the standard normal:

$$
dW \sim \mathcal{N}(0, I dt)
$$

Last Reviewed: 10/3/2026
