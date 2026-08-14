# LayerNorm
1. Input and output: Batch x model_dim (N,D).
2. Batch is treated like a batch-like dimension the whole time.
3. We normalize each of the N vectors by demeaning it and dividing by its standard deviation.
4. We then take it multiplied by beta, gamma, which are model_dim shift and scale vectors


# RMSNorm
1. Input and output: Batch x model_dim (N,D).
2. Similar to LayerNorm, but no demeaning, and no shift parameter.
3. Like projecting all N vectors on to a D-dimensional hypersphere (then scaling)

# BatchNorm

## Basic
1. Input and output: Batch x model_dim (N,D).
2. Equivalent to transposed layernorm, but beta and gamma remain still model_dim.
3. During training, running mean and variance are updated. The batch variance is multiplied by (N/(N-1)) before contributing to the update.

## 2D (used in compute vision)
1. Input and output: (N, C, H, W)
2. Equivalent to batch norm, but H and W are treated as part of the batch.