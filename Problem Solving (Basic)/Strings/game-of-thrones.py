from collections import Counter


def gameOfThrones(s):
    counter = Counter(s)
    if len(s) % 2 == 0:
        result = all([x % 2 == 0 for x in counter.values()])
    else:
        if len(list(filter(lambda x: x % 2 == 1, counter.values()))) == 1:
            result = True
        else:
            result = False

    return 'YES' if result else 'NO'
