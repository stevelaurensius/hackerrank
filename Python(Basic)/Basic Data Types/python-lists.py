if __name__ == '__main__':
    loop_input = int(input(''))
    counter = 1
    container = []
    while counter <= loop_input:
        user_input = input().split()
        if user_input[0] == 'append':
            container.append(int(user_input[1]))
        if user_input[0] == 'print':
            print(container)
        if user_input[0] == 'insert':
            container.insert(int(user_input[1]), int(user_input[2]))
        if user_input[0] == 'remove':
            for i in container:
                container.remove(int(user_input[1]))
                break
        if user_input[0] == 'sort':
            container.sort()
        if user_input[0] == 'pop':
            container.pop(-1)
        if user_input[0] == 'reverse':
            container.reverse()
        counter += 1
