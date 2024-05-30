def average(array):
    returned_value = sum(set(array)) / len(set(array))
    return returned_value


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)