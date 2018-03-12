def matrixElementsSum(matrix):
    for i in range(len(matrix)-1):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                for k in range(i, len(matrix)):
                    matrix[k][j] = 0

    return sum(sum(matrix, []))
