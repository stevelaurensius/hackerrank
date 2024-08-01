def appendAndDelete(s, t, k):
    counter = 0
    while counter < min(len(s), len(t)) and s[counter] == t[counter]:
        counter += 1
    x = len(s) + len(t) - (2 * counter)
    if x <= k and ((k - x) % 2 == 0 or (len(s) + len(t)) <= k):
        return "Yes"
    else:
        return "No"
