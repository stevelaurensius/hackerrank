def solve(s):
    splitted = s.split(' ')
    result = []
    for word in splitted:
        if word != '':
            result.append(word[0].upper() + word[1:])
        else:
            result.append(word)
    return ' '.join(result)
