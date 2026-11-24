# Дерево = связный граф с N-1 рёбрами

# Читаем количество вершин и рёбер
n, m = map(int, input().split())

# Создаём список смежности
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

# n-1 рёбер
if m != n - 1:
    print("NO")
else:
    # граф - связный
    # связность через BFS
    visited = [False] * (n + 1)
    queue = [1]  # начинаем с вершины 1
    visited[1] = True
    count = 1  # количество посещённых вершин

    while queue:
        v = queue.pop(0)
        for u in adj[v]:
            if not visited[u]:
                visited[u] = True
                count += 1
                queue.append(u)

    # Если посетили все вершины — граф связный
    if count == n:
        print("YES")
    else:
        print("NO")