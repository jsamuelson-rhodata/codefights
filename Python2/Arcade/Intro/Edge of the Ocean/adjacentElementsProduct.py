def adjacentElementsProduct(inputArray):
    return max([inputArray[i] * inputArray[i+1] for i in xrange(len(inputArray)-1)])
