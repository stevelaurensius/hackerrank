height, width = map(int, input().split())
pattern = '.|.'
stripe = '-'
center_text = 'WELCOME'
counter = 1

for _ in (range(height // 2)):
    print((pattern * counter).center(width, stripe))
    counter += 2

print(center_text.center(width, stripe))
counter -= 2

for _ in (range(height // 2)):
    print((pattern * counter).center(width, stripe))
    counter -= 2
