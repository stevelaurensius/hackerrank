def introTutorial(V, arr):
    return arr.index(V)


if __name__ == '__main__':
    V = 4
    n = 6
    arr = [1, 4, 5, 7, 9, 12]
    result = introTutorial(V, arr)
    print(result)
