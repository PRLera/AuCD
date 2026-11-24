#кратчайший путь на доске(на Н похожа)

from collections import deque
import sys

# Читаем числа из всего ввода
data = sys.stdin.read().split()
n = int(data[0])
x1 = int(data[1])
y1 = int(data[2])
x2 = int(data[3])
y2 = int(data[4])

# Все 8 возможных ходов коня
moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
         (1, -2), (1, 2), (2, -1), (2, 1)]

# BFS
# True если клетка уже посещена
visited = [[False] * (n + 1) for _ in range(n + 1)]
parent = {}

queue = deque([(x1, y1)])
visited[x1][y1] = True
parent[(x1, y1)] = None

found = False

while queue:
    x, y = queue.popleft()

    if x == x2 and y == y2: #дошли до конца
        found = True
        break

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 1 <= nx <= n and 1 <= ny <= n and not visited[nx][ny]:
            visited[nx][ny] = True
            parent[(nx, ny)] = (x, y)
            queue.append((nx, ny))

if not found:
    print(-1)
else:
    # Восстанавливаем путь,от конца к началу через предков
    path = []
    v = (x2, y2)
    while v is not None:
        path.append(v)
        v = parent[v]
    path.reverse()

    # Выводим количество ходов
    print(len(path) - 1)
    # Выводим путь
    for x, y in path:
        print(x, y)