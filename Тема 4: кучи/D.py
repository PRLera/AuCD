import heapq

heap = []

while True:
    try:
        command = input().split()
    except EOFError:
        break

    if not command:
        continue

    cmd = command[0]

    if cmd == 'CLEAR':
        heap.clear()

    elif cmd == 'ADD':
        n = int(command[1])
        heapq.heappush(heap, -n)

    elif cmd == 'EXTRACT':
        if len(heap) == 0:
            print('CANNOT')
        else:
            max_val = -heapq.heappop(heap)
            print(max_val)