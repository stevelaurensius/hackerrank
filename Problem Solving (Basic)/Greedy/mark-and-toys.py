def maximumToys(prices, k):
    prices = sorted(prices)
    result = 0
    for i in prices:
        if k - i >= 0:
            k -= i
            result += 1
        else:
            break
    return result
