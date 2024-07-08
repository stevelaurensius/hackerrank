def staircase(n):
    for line in range(n):
        text = '#' * (line + 1)
        print(text.rjust(n))