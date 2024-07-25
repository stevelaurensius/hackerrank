def divisibleSumPairs(n, k, arr):
    remainder_count = [0] * k
    count = 0

    for data in arr:
        remainder = data % k
        complement = (k - remainder) % k
        count += remainder_count[complement]
        remainder_count[remainder] += 1

    return count
