def permutationEquation(p):
    result = []
    for i in range(len(p)):
        first = p.index(i + 1)
        second = first + 1
        third = p.index(second)
        result.append(third + 1)
    return result
