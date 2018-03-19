def allLongestStrings(inputArray):
    return [i for i in inputArray if len(i) == max(len(j) for j in inputArray)]
