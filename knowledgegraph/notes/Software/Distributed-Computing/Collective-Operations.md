# Legend
1. Each row is one rank (a device/GPU)
2. Each column is a slot in a buffer (e.g. a chunk or row of a tensor)
3. Number says what rank produced the data
4. Letter says which chunk it is
5. Blank means that the device has no valid data in that slot




# Gather
Think of this as a single tensor being sharded across three ranks. Gather takes all the pieces and collects them as a big tensor on the root rank.

1. 1 _ _ --> 1 2 3
2. _ 2 _ --> _ 2 _
3. _ _ 3 --> _ _ 3


# All-Gather
Same as gather, but all-gather does it on all ranks

1. 1 _ _ --> 1 2 3
2. _ 2 _ --> 1 2 3
3. _ _ 3 --> 1 2 3


# Reduce
Essentially sums across ranks and stores the result on the first rank

1. 1a 1b 1c --> (1a + 2a + 3a) (1b + 2b + 3b) (1c + 2c + 3c)
2. 2a 2b 2c --> 2a             2b             2c
3. 3a 3b 3c --> 3a             3b             3c


# All-Reduce
Same as reduce, but does it on all ranks

1. 1a 1b 1c --> (1a + 2a + 3a) (1b + 2b + 3b) (1c + 2c + 3c)
2. 2a 2b 2c --> (1a + 2a + 3a) (1b + 2b + 3b) (1c + 2c + 3c)
3. 3a 3b 3c --> (1a + 2a + 3a) (1b + 2b + 3b) (1c + 2c + 3c)


# Scatter
Takes a big tensor and shards it into smaller tensors across ranks

1. 1a 1b 1c --> 1a _  _
2. _  _  _  --> _  1b _
3. _  _  _  --> _  _  1c



# Reduce-Scatter
1. 1a 1b 1c --> (1a + 2a + 3a) _              _
2. 2a 2b 2c --> _              (1b + 2b + 3b) _
3. 3a 3b 3c --> _              _              (1c + 2c + 3c)

Source: https://en.wikipedia.org/wiki/Collective_operation
Last Reviewed: 9/27/2026
