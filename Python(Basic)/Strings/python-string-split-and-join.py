def split_and_join(x):
    split_string = x.split()
    join_string = "-".join(split_string)
    return join_string


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
