def arrayMaxConsecutiveSum(a, k):
    crnt_sum = max_sum = sum(a[:k])
    
    for i in range(len(a) - k):
        crnt_sum = crnt_sum + a[i + k] - a[i]
        max_sum = max(crnt_sum, max_sum)
        
    return max_sum
