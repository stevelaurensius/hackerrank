def mutate_string(string, position, character):
    result = list(string)
    result.insert(position, character)
    del result[position + 1]
    result = ''.join(result)
    return result


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
