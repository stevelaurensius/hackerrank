def swap_case(s):
    return_result = ''
    for char in s:
        if char.isupper():
            return_result += char.lower()
        elif char.islower():
            return_result += char.upper()
        else:
            return_result += char
    return return_result


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
