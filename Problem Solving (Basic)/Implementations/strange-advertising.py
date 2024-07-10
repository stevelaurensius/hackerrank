import math

def viralAdvertising(n):
    cumulative = 0
    liked = 0
    for i in range(n):
        if i == 0:
            shared = 5
            liked = math.floor(shared/2)
            cumulative += liked
        else:
            shared = liked * 3
            liked = math.floor(shared/2)
            cumulative += liked
    return cumulative


if __name__ == '__main__':
    n = int(input().strip())
    result = viralAdvertising(n)
    print(result)
