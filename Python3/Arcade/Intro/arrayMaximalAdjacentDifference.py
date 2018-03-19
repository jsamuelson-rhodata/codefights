def arrayMaximalAdjacentDifference(inputArray):
    return max([abs(i - j) for i,j in zip(inputArray, inputArray[1:])])
