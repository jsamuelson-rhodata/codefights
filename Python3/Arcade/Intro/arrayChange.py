def arrayChange(inputArray):
    moves = 0
    for i in range(len(inputArray)-1):
        if inputArray[i+1] <= inputArray[i]:
            moves += inputArray[i] - inputArray[i+1] + 1
            inputArray[i+1] = inputArray[i] + 1
    return moves
