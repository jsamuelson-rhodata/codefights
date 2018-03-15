def isLucky(n):
    digits = [int(i) for i in list(str(n))]
    return sum(digits[:len(digits)/2]) == sum(digits[len(digits)/2:])
