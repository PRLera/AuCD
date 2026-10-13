deck = []

while True:
    command = input().split()
    cmd = command[0]

    if cmd == 'push_front':
        n = int(command[1])
        deck.insert(0, n)
        print('ok')

    elif cmd == 'push_back':
        n = int(command[1])
        deck.append(n)
        print('ok')

    elif cmd == 'pop_front':
        if len(deck) == 0:
            print('error')
        else:
            print(deck.pop(0))

    elif cmd == 'pop_back':
        if len(deck) == 0:
            print('error')
        else:
            print(deck.pop())

    elif cmd == 'front':
        if len(deck) == 0:
            print('error')
        else:
            print(deck[0])

    elif cmd == 'back':
        if len(deck) == 0:
            print('error')
        else:
            print(deck[-1])

    elif cmd == 'size':
        print(len(deck))

    elif cmd == 'clear':
        deck.clear()
        print('ok')

    elif cmd == 'exit':
        print('bye')
        break