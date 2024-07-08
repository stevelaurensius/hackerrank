def hurdleRace(k, height):
    tallest = max(height)
    if tallest - k <= 0:
        return 0
    return tallest - k
