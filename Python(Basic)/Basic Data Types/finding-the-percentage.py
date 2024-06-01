if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # student_marks = {'Harsh': [25.0, 26.5, 28.0], 'Anurag': [26.0, 28.0, 30.0]}
    # query_name = 'Anurag'

    counter = 0
    result = 0
    for i in student_marks[query_name]:
        result += student_marks[query_name][counter]
        counter += 1
    result /= len(student_marks[query_name])
    formatted_result = "{:.2f}".format(result)
    print(formatted_result)
