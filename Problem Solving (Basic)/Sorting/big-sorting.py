def bigSorting(unsorted):
    sorted_ = sorted([int(x) for x in unsorted])
    sorted_str = ([str(x) for x in sorted_])
    return sorted_str


if __name__ == '__main__':
    n = int(input().strip())
    unsorted = []
    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)
    result = bigSorting(unsorted)
    print('\n'.join(result))
