# Legend
1. Each row is one device (a rank)
2. Each column is a slot in a buffer (e.g. a chunk of a tensor)
3. Letter says what GPU produced the data
4. Number says which chunk it is
5. Blank means that the device has no valid data in that slot




# Gather
1. a1 _  _  -->  a1 a2 a3
2. _  a2 _  -->  _  a2 _
3. _  _  a3 -->  _  _  a3

# All-Gather
1. a1 _  _  --> a1 a2 a3
2. _  a2 _  --> a1 a2 a3
3. _  _  a3 --> a1 a2 a3


# Reduce
1. a1 a2 a3 --> (a1 + b1 + c1) (a2 + b2 + c2) (a3 + b3 + c3)
2. b1 b2 b3 --> b1             b2             b3
3. c1 c2 c3 --> c1             c2             c3


# All-Reduce
1. a1 a2 a3 --> (a1 + b1 + c1) (a2 + b2 + c2) (a3 + b3 + c3)
2. b1 b2 b3 --> (a1 + b1 + c1) (a2 + b2 + c2) (a3 + b3 + c3)
3. c1 c2 c3 --> (a1 + b1 + c1) (a2 + b2 + c2) (a3 + b3 + c3)

# Scatter
1. a1 a2 a3 --> a1 _  _
2. _  _  _  --> _  a2 _
3. _  _  _  --> _  _  a3



# Reduce-Scatter
1. a1 a2 a3 --> (a1 + b1 + c1) _              _
2. b1 b2 b3 --> _              (a2 + b2 + c2) _
3. c1 c2 c3 --> _              _              (a3 + b3 + c3)

Source: https://en.wikipedia.org/wiki/Collective_operation
Last Reviewed: 9/27/2026
