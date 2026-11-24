# тоже самое что и М(про столы)

from collections import deque

# Читаем количество студентов и пар
n, m = map(int, input().split())

# Создаём список смежности
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

# Раскраска в 2 цвета (BFS)
color = [-1] * (n + 1)

# Проверяем все компоненты (граф может быть несвязным)
is_bipartite = True

for start in range(1, n + 1):
    if color[start] == -1:
        color[start] = 0
        queue = deque([start])

        while queue:
            v = queue.popleft()
            for u in adj[v]:
                if color[u] == -1:
                    color[u] = 1 - color[v]
                    queue.append(u)
                elif color[u] == color[v]:
                    is_bipartite = False
                    break
            if not is_bipartite:
                break
        if not is_bipartite:
            break

# (не выводим что-то конкретное, только да или нет)
if is_bipartite:
    print("YES")
else:
    print("NO")