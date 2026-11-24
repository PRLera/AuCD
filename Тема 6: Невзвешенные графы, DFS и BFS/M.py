#Раскрашиваем граф в 2 цвета. Если конфликт — не двудольный (2 стола, можно ли рассадить гостей, чтобы пары конфликтующие, не вместе)

from collections import deque

# Читаем количество гостей и пар
n, m = map(int, input().split())

# Создаём список смежности
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

# Раскраска в 2 цвета (BFS)
color = [-1] * (n + 1)  # -1 = не раскрашен, 0 или 1 = цвет
is_bipartite = True #двудольный

# Проходим по всем компонентам
for start in range(1, n + 1):
    if color[start] == -1:
        color[start] = 0
        queue = deque([start])

        while queue and is_bipartite:
            v = queue.popleft()
            for u in adj[v]:
                if color[u] == -1:
                    color[u] = 1 - color[v] #противополож цвет
                    queue.append(u)
                elif color[u] == color[v]: # один цвет-конфликт
                    is_bipartite = False
                    break

if is_bipartite:
    print("YES")
    # Собираем вершины первого стола (цвет 0)
    table1 = [i for i in range(1, n + 1) if color[i] == 0]
    print(' '.join(map(str, table1)))
else:
    print("NO")