def pickingNumbers(a):
    pool = [0 for _ in range(100)]
    for i in a:
        pool[i] += 1
    result = 0
    for i in range(1, 99):
        result = max(result, pool[i] + pool[i+1])
    return result
