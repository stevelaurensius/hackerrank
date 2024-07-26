def angryProfessor(k, a):
    counter = 0
    for data in a:
        if data <= 0:
            counter += 1
    if counter < k:
        return 'YES'
    else:
        return 'NO'
