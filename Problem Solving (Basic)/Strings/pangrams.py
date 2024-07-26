def pangrams(s):
    result = set(s.lower())
    if len(result) == 27:
        return 'pangram'
    elif len(result) != 27:
        return 'not pangram'
