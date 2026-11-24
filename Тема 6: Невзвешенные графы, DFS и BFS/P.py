#граф — это матрица, клетки — вершины, соседи — клетки рядом

from collections import deque

# Читаем размеры лабиринта
n, m = map(int, input().split())

# Читаем лабиринт
maze = []
for i in range(n):
    row = list(map(int, input().split()))
    maze.append(row)

# BFS
# dist[i][j] = расстояние от (0,0) до (i,j), -1 = не посещено
dist = [[-1] * m for _ in range(n)] #матрица расстояний
dist[0][0] = 0

# (строка, столбец)
queue = deque([(0, 0)])

# 4 направления: вверх, вниз, влево, вправо
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while queue:
    x, y = queue.popleft()

    # Если дошли до правого нижнего угла
    if x == n - 1 and y == m - 1:
        break

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        # Проверяем границы, клетка свободна и не посещена
        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 0 and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            queue.append((nx, ny))

# Выводим расстояние
print(dist[n - 1][m - 1])