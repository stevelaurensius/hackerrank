n = int(input())
s = set(map(int, input().split()))

no_of_command = int(input())
for i in range(no_of_command):
    command = input()
    if command == 'pop':
        s.pop()
    else:
        instruction, x = command.split()
        methods = {'remove': s.remove, 'discard': s.discard}
        methods[instruction](int(x))
print(sum(s))