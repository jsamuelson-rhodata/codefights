from itertools import permutations

def char_diff1(str1, str2):
    return sum([pair[0] != pair[1] for pair in zip(str1, str2)]) == 1

def stringsRearrangement(inputArray):
    for i in permutations(inputArray):
        if sum([char_diff1(*j) for j in zip(i, i[1:])]) == len(inputArray) - 1:
            return True
    return False
