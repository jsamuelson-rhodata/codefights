def isIPv4Address(inputString):
    addr = inputString.split(".")
    return len(addr) == 4 and all(i.isdigit() and 0 <= int(i) <= 255 for i in addr)
