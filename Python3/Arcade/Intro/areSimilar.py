def areSimilar(a, b):
    return sorted(a) == sorted(b) and sum([i != j for i,j in zip(a,b)]) < 3
