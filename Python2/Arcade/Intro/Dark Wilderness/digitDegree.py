def digitDegree(n):
    t = 0
    while n > 9:
        n = sum(int(i) for i in str(n))
        t += 1
    return t
