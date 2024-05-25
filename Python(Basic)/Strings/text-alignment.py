width = int(input())
char = 'H'
arrow_width = (2 * width) - 1
spacer = width * 4

for i in range(width):
    new_char = char * ((i * 2) +1)
    upper_pyramid = new_char.center(arrow_width, ' ')
    print(upper_pyramid.rstrip())

for i in range(width + 1):
    upper_hand = (char * width).center(arrow_width, ' ') + (' ' * (width * 2 + 1)) + (char * width).center(arrow_width, ' ')
    print(upper_hand.rstrip())

for i in range((width + 1) // 2):
    middle_body = (char * (width * 5)).center(width * 6 - 1, ' ')
    print(middle_body.rstrip())

for i in range(width + 1):
    lower_hand = (char * width).center(arrow_width, ' ') + (' ' * (width * 2 + 1)) + (char * width).center(arrow_width, ' ')
    print(lower_hand.rstrip())

for i in range(width):
    new_char = char * ((width * 2) - 1)
    lower_pyramid = (' ' * spacer) + new_char.center(arrow_width, ' ')
    print(lower_pyramid.rstrip())
    width -= 1
