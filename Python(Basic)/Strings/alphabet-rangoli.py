def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase

    width = 4 * size - 3

    pattern = []
    for i in range(size):
        s = '-'.join(alpha[size-1:i:-1] + alpha[i:size])
        pattern.append((s.center(width, '-')))

    print('\n'.join(pattern[:0:-1] + pattern))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
