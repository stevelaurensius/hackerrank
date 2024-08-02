def squares(a, b):
    batas_bawah = math.ceil(math.sqrt(a))
    batas_atas = math.floor(math.sqrt(b))
    return batas_atas - batas_bawah + 1
