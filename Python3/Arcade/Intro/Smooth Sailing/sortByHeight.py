def sortByHeight(a):
    ppl_sorted = sorted([i for i in a if i > 0])
    for i, n in enumerate(a):
        if n < 0:
            ppl_sorted.insert(i, n)
    return ppl_sorted
