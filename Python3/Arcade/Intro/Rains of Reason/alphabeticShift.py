def alphabeticShift(inputString):
    return "".join(chr((ord(i) - 96) % 26 + 97) for i in inputString)
