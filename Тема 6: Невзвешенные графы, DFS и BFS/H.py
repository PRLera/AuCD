from collections import deque

# Читаем количество вершин
n = int(input())

# Читаем матрицу смежности
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# начальная и конечная вершины
start, end = map(int, input().split())

# Если начальная и конечная вершины совпадают, длинна 0
if start == end:
    print(0)
else:
    # BFS
    visited = [False] * (n + 1)
    parent = [0] * (n + 1)  # предок каждой вершины
    queue = deque([start])
    visited[start] = True

    found = False

    while queue:
        v = queue.popleft()

        if v == end: #дошли до конца, выходим
            found = True
            break

        for u in range(1, n + 1):
            if matrix[v - 1][u - 1] == 1 and not visited[u]:# есть ребро и не посещали
                visited[u] = True
                parent[u] = v  #запоминаем, откуда пришли
                queue.append(u)

    if not found:# путь не найден
        print(-1)
    else:
        # Восстанавливаем путь, от конца к началу через предков
        path = []
        v = end
        while v != 0:
            path.append(v)
            v = parent[v]
        path.reverse()#разворачиваем

        # Выводим длину пути (количество рёбер)
        print(len(path) - 1)
        #  путь
        print(' '.join(map(str, path)))