def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    check_number = False
    check_lower_case= False
    check_upper_case = False
    check_special_char = False
    for char in password:
        if char in lower_case:
            check_lower_case = True
        if char in numbers:
            check_number = True
        if char in upper_case:
            check_upper_case = True
        if char in special_characters:
            check_special_char = True
    result = [check_lower_case, check_number, check_upper_case, check_special_char]
    final_result = result.count(False)
    if n >= 6:
        return final_result
    if n < 6:
        if n + final_result < 6:
            return 6 - n
        elif n + final_result >= 6:
            return final_result