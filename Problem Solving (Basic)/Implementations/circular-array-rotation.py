def circularArrayRotation(a, k, queries):
    x = k % len(a)
    a = a[-x:] + a[:-x]
    result = []
    for i in queries:
        result.append(a[i])
    return result
