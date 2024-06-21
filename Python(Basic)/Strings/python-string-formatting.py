def print_formatted(number):
    pad_width = len(str(bin(n))) - 2
    for i in range(n):
        n_ = str(i + 1).rjust(pad_width, " ")
        oct_ = oct(i + 1)[2:].rjust(pad_width, " ")
        hex_ = hex(i + 1)[2:].upper().rjust(pad_width, " ")
        bin_ = bin(i + 1)[2:].rjust(pad_width, " ")
        print(n_, oct_, hex_, bin_)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
