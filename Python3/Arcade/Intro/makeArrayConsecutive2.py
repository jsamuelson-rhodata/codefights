def makeArrayConsecutive2(statues):
    return len(list(range(min(statues), max(statues)+1))) - len(statues)
