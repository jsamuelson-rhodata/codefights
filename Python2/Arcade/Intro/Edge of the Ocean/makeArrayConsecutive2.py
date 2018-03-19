def makeArrayConsecutive2(statues):
    return len(range(min(statues), max(statues)+1)) - len(statues)
