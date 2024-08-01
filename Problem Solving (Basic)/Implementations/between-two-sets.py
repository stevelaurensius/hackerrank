def getTotalX(a, b):
    result = 0
    for i in range(max(a), min(b) + 1):
        if all([i % aa == 0 for aa in a]) and all([bb % i == 0 for bb in b]):
            result += 1
    return result
