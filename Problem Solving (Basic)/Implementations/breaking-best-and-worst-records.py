def breakingRecords(scores):
    highest_score = 0
    lowest_score = 0
    high_score = 0
    low_score = 0

    for i in range(len(scores)):
        if i == 0:
            highest_score = scores[i]
            lowest_score = scores[i]
        if scores[i] > highest_score:
            high_score += 1
            highest_score = scores[i]
        if scores[i] < lowest_score:
            low_score += 1
            lowest_score = scores[i]
    return high_score, low_score
