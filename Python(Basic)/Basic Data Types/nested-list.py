if __name__ == '__main__':
    result_list = []
    score_list = []
    final_list = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        result_list.append([name, score])
        score_list.append(score)
        score_list = list(set(score_list))
        score_list.sort()

    final_list = [item[0] for item in result_list if item[1] == score_list[1]]
    final_list.sort()
    for i in final_list:
        print(i)
