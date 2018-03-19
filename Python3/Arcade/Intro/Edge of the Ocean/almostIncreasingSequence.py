def almostIncreasingSequence(sequence):
    return 3 > sum((i >= j) + (i >= k) for i, j, k in zip(sequence, sequence[1:], sequence[2:] + [1e6]))
