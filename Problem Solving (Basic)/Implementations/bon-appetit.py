def bonAppetit(bill, k, b):
    shared_bill = sum([value for index, value in enumerate(bill) if index != k]) / 2
    if b == shared_bill:
        print('Bon Appetit')
    else:
        print(int(b - shared_bill))