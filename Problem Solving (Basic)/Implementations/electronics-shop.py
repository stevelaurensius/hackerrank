def getMoneySpent(keyboards, drives, b):
    possibility = [x + y for x in keyboards for y in drives]
    possibility.sort(reverse=True)
    for i in possibility:
        if i <= b:
            return i
    return -1
