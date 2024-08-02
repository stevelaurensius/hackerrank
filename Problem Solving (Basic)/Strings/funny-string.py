def funnyString(s):
    ord_list = [ord(x) for x in s]
    ord_result = []
    for i in range(len(ord_list) - 1):
        ord_result.append(abs(ord_list[i] - ord_list[i + 1]))

    rev_list = list(reversed(ord_list))
    rev_result = []
    for i in range(len(rev_list) - 1):
        rev_result.append(abs(rev_list[i] - rev_list[i + 1]))

    if ord_result == rev_result:
        return 'Funny'
    elif ord_result != rev_result:
        return 'Not Funny'
