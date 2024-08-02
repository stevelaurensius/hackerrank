from collections import Counter


def makingAnagrams(s1, s2):
    result = 0

    count_s1 = Counter(s1)
    count_s2 = Counter(s2)
    counter = {}

    for letter, value in count_s1.items():
        counter[letter] = abs(value - count_s2[letter])
    for letter, value in count_s2.items():
        counter[letter] = abs(value - count_s1[letter])

    for i in counter.values():
        result += i

    return result
