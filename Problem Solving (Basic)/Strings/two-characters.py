from itertools import combinations


def alternate(s):
    s_set = set(s)
    combination_possibilities = combinations(s_set, 2)

    def validate(s):
        for ind in range(len(s) - 1):
            if s[ind] == s[ind + 1]:
                return False
        return True

    max_result = 0
    for comb in combination_possibilities:
        t = [x for x in s if x == comb[0] or x == comb[1]]
        if validate(t):
            max_result = max(max_result, len(t))
    return max_result
