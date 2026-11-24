#Подсчёт компонент связности на матрице(на сколько кусков распадется лист после удаления некоторых клеток)

# Читаем размеры листа
m, n = map(int, input().split())

# Читаем лист
sheet = []
for i in range(m):
    row = input().strip()
    sheet.append(row)

# True если клетка уже посещена
visited = [[False] * n for _ in range(m)]

# Счётчик кусков
pieces = 0

# 4 направления: вверх, вниз, влево, вправо
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Проходим по всем клеткам
for i in range(m):
    for j in range(n):
        # Если клетка осталась (#) и не посещена — новый кусок
        if sheet[i][j] == '#' and not visited[i][j]:
            pieces += 1

            # DFS через стек
            stack = [(i, j)]
            visited[i][j] = True

            while stack:
                x, y = stack.pop()#клетка из стека
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and sheet[nx][ny] == '#':
                        visited[nx][ny] = True
                        stack.append((nx, ny))

print(pieces)