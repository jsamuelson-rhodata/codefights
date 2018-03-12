def matrixElementsSum(matrix):
    for i in xrange(len(matrix)-1):
        for j in xrange(len(matrix[i])):
            if matrix[i][j] == 0:
                for k in xrange(i, len(matrix)):
                    matrix[k][j] = 0

    return sum(sum(matrix, []))
