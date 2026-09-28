# Gather
1. a --> a b c
2. b --> b
3. c --> c

# All-Gather
1. a --> a b c
2. b --> a b c
3. c --> a b c

# Reduce
1. a --> a + b + c or some other reducing operation
2. b --> b
3. c --> c 


# All-Reduce
1. a --> a + b + c
2. b --> a + b + c
3. c --> a + b + c


# Scatter
1. a b c --> a
2. --> b
3. --> c


# Reduce-Scatter
1. a1 a2 a3 --> a1 + b1 + c1
2. b1 b2 b3 --> a2 + b2 + c2
3. c1 c2 c3 --> a3 + b3 + c3

Source: https://en.wikipedia.org/wiki/Collective_operation
Last Reviewed: 9/27/2026
