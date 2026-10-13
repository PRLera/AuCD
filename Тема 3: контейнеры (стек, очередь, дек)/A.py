stack = []

while True:
    command = input().split()
    cmd = command[0]

    if cmd == 'push':
        n = int(command[1])
        stack.append(n)
        print('ok')

    elif cmd == 'pop':
        if len(stack) == 0:
            print('error')
        else:
            print(stack.pop())

    elif cmd == 'back':
        if len(stack) == 0:
            print('error')
        else:
            print(stack[-1])

    elif cmd == 'size':
        print(len(stack))

    elif cmd == 'clear':
        stack.clear()
        print('ok')

    elif cmd == 'exit':
        print('bye')
        break