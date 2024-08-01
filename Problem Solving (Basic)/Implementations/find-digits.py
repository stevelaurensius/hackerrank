def findDigits(n):
    factor = list(str(n))
    result = [n % int(x) == 0 for x in factor if int(x) != 0]
    return sum(result)
