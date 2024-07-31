def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_total = 0
    orange_total = 0
    for apple in apples:
        if s <= a + apple <= t:
            apple_total += 1
    for orange in oranges:
        if s <= b + orange <= t:
            orange_total += 1
    print(apple_total)
    print(orange_total)
