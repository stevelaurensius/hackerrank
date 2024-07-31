def gradingStudents(grades):
    grades_list = grades
    result = []
    for grade in grades_list:
        if grade >= 37:
            if grade % 5 == 0:
                result.append(grade)
            elif (grade + 2) % 5 == 0:
                result.append(grade + 2)
            elif (grade + 1) % 5 == 0:
                result.append(grade + 1)
            else:
                result.append(grade)
        else:
            result.append(grade)
    return result
