def caesarCipher(s, k):
    difference = k  % 26
    original_string = s
    original_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    modified_alphabet = original_alphabet[difference:] + original_alphabet[:difference]
    final_string = ''
    for char in original_string:
        if char.lower() in original_alphabet:
            index = original_alphabet.index(char.lower())
            if char.isupper():
                final_string += modified_alphabet[index].upper()
            else:
                final_string += modified_alphabet[index]
        else:
            final_string += char
    return final_string
