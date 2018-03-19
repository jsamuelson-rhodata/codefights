def minesweeper(matrix):
    out = []
    for i in xrange(len(matrix)):
        out.append([])
        for j in xrange(len(matrix[0])):
            l = -matrix[i][j]
            for x in [-1,0,1]:
                for y in [-1,0,1]:
                    if 0 <= i + x < len(matrix) and 0 <= j + y < len(matrix[0]):
                        l += matrix[i+x][j+y]

            out[i].append(l)
    return out
              
