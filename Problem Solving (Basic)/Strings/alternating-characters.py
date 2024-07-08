def alternatingCharacters(s):
    counter = 0
    for index in range(len(s) - 1):
        if s[index] == s[index + 1]:
            counter += 1
    return counter
