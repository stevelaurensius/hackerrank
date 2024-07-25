def marsExploration(s):
    str_length = len(s)
    correct_list = []
    counter = 0
    while len(correct_list) < str_length:
        correct_list.extend(list('SOS'))
    for index in range(len(correct_list)):
        if s[index] != correct_list[index]:
            counter += 1
    return counter
