def compareTriplets(a, b):
    a_points = 0
    b_points = 0
    for indexes in range(3):
        if a[indexes] > b[indexes]:
            a_points += 1
        if a[indexes] < b[indexes]:
            b_points += 1
    return a_points, b_points