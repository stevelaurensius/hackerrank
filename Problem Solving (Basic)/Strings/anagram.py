from collections import Counter


def anagram(s):
    if len(s) % 2 != 0:
        return -1

    first_part = Counter(s[:(len(s) // 2)])
    second_part = Counter(s[(len(s) // 2):])
    counter = {}
    result = 0

    for letter, value in first_part.items():
        counter[letter] = abs(value - second_part[letter])
    for letter, value in second_part.items():
        counter[letter] = abs(value - first_part[letter])

    for i in counter.values():
        result += i
    return result // 2
