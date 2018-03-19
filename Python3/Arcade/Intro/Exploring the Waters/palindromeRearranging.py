def palindromeRearranging(inputString):
    return sum([inputString.count(c) % 2 for c in set(inputString)]) < 2
