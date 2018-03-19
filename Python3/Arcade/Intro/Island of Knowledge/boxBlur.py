def boxBlur(image):
    nrow = len(image)
    ncol = len(image[0])
    out = []
    for i in xrange(1, nrow-1):
        row = []
        for j in xrange(1, ncol-1):
            row.append(sum([image[i+k][j+l] for k in [-1,0,1] for l in [-1,0,1]]) / 9)
        out.append(row)
    return out
