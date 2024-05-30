if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list_arr = list(arr)
    unique_arr = list(set(list_arr))
    unique_arr.sort()
    print(unique_arr[-2])
