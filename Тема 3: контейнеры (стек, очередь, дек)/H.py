import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

left = deque()  # первая половина очереди
right = deque()  # вторая половина очереди
output = []  # сюда копируем ответы

for _ in range(n):
    line = input().split()

    if line[0] == '+':
        # Обычный гоблин — в конец очереди
        right.append(int(line[1]))
        # Баланс: если right стал больше left, перекладываем
        if len(right) > len(left):
            left.append(right.popleft())

    elif line[0] == '*':
        # Привилегированный гоблин — сразу за центром
        right.appendleft(int(line[1]))
        # Баланс: если right стал больше left, перекладываем
        if len(right) > len(left):
            left.append(right.popleft())

    else:  # '-'
        # Первый гоблин уходит
        output.append(str(left.popleft()))
        # Баланс: если left стал меньше right, перекладываем
        if len(left) < len(right):
            left.append(right.popleft())

# Выводим все ответы сразу (быстро!)
print('\n'.join(output))