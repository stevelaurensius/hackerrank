def repeatedString(s, n):
    repeats = (n // len(s))
    result = repeats * sum(c == 'a' for c in s)
    for i in range(n - (repeats * len(s))):
        result += (s[i] == 'a')
    return result
