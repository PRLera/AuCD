queue = []

while True:
    command = input().split()
    cmd = command[0]

    if cmd == 'push':
        n = int(command[1])
        queue.append(n)
        print('ok')

    elif cmd == 'pop':
        if len(queue) == 0:
            print('error')
        else:
            print(queue.pop(0))

    elif cmd == 'front':
        if len(queue) == 0:
            print('error')
        else:
            print(queue[0])

    elif cmd == 'size':
        print(len(queue))

    elif cmd == 'clear':
        queue.clear()
        print('ok')

    elif cmd == 'exit':
        print('bye')
        break