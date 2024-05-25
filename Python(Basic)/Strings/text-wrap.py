import textwrap


def wrap(string, max_width):
    result = ''
    temp_result = textwrap.wrap(string, width=max_width)
    for i in temp_result:
        result += i + '\n'
    return result


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
