def plusMinus(arr):
    pos = len([x for x in arr if x > 0]) / len(arr)
    neg = len([x for x in arr if x < 0]) / len(arr)
    zer = len([x for x in arr if x == 0]) / len(arr)
    print(format(pos, ".6f"))
    print(format(neg, ".6f"))
    print(format(zer, ".6f"))