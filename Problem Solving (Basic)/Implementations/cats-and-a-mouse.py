def catAndMouse(x, y, z):
    cat_a_position = x
    cat_b_position = y
    mouse_position = z
    cat_a_to_mouse = abs(cat_a_position - mouse_position)
    cat_b_to_mouse = abs(cat_b_position - mouse_position)
    if cat_a_to_mouse < cat_b_to_mouse:
        return 'Cat A'
    elif cat_b_to_mouse < cat_a_to_mouse:
        return 'Cat B'
    elif cat_a_to_mouse == cat_b_to_mouse:
        return 'Mouse C'
