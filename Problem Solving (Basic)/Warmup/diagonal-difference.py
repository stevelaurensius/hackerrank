def diagonalDifference(arr):
    primary_diagonal = 0
    secondary_diagonal = 0
    index = 0
    reverse_index = -1
    for row in arr:
        primary_diagonal += row[index]
        index += 1
    for row in arr:
        secondary_diagonal += row[reverse_index]
        reverse_index -= 1
    return abs(primary_diagonal - secondary_diagonal)