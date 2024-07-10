def designerPdfViewer(h, word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result_list = []
    for char in word:
        result_list.append(h[alphabet.index(char)])
    return max(result_list) * len(result_list)
