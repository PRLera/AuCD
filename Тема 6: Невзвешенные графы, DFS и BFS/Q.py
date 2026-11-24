# Тоже, что P, но один ход = скольжение до упора

from collections import deque

# Читаем размеры
n, m = map(int, input().split())

# Читаем лабиринт
maze = []
for i in range(n):
    row = list(map(int, input().split()))
    maze.append(row)

# BFS
# dist[i][j] = расстояние от (0,0) до (i,j), -1 = не посещено
dist = [[-1] * m for _ in range(n)]
dist[0][0] = 0

queue = deque([(0, 0)])

# 4 направления
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

answer = -1 #пути нет

while queue:
    x, y = queue.popleft()

    # Пробуем все 4 направления
    for dx, dy in directions:
        # Скользим в направлении (dx, dy)
        nx, ny = x, y

        while True:
            next_x, next_y = nx + dx, ny + dy
            # Проверяем, можно ли продолжить скольжение
            if 0 <= next_x < n and 0 <= next_y < m and maze[next_x][next_y] != 1:
                nx, ny = next_x, next_y
                # Проверяем, не отверстие ли это
                if maze[nx][ny] == 2:# отверстие на пути
                    if answer == -1 or dist[x][y] + 1 < answer:
                        answer = dist[x][y] + 1
                    break
            else:
                break

        # Если шарик не провалился в отверстие и сдвинулся
        if maze[nx][ny] != 2 and (nx, ny) != (x, y) and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            queue.append((nx, ny))

print(answer)