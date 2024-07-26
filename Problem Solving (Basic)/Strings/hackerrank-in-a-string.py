def hackerrankInString(s):
    string_check = 'hackerrank'
    index_check = 0
    final_result = ''
    for i in s:
        if i == string_check[index_check]:
            final_result += i
            index_check += 1
        if final_result == string_check:
            return 'YES'
    return 'NO'
