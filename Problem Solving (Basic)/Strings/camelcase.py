def camelcase(s):
    counter = 1
    for char in s:
        if char.isupper():
            counter += 1
    return counter
