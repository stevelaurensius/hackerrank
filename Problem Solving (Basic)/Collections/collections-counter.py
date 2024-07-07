from collections import Counter

income_ = 0
number_of_data = int(input())
data_input = str(input())
data_list = dict(Counter(data_input.split()))
number_of_buyer = int(input())
for number in range(number_of_buyer):
    size, income = input().split()
    if size not in data_list.keys():
        pass
    elif data_list[size] >= 1:
        data_list[size] -= 1
        income_ += int(income)

print(income_)