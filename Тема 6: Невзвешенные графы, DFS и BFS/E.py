#Найти все компоненты связности в неориентированном графе

from collections import deque

# количество вершин и рёбер
n, m = map(int, input().split())

# список смежности
adj = [[] for _ in range(n + 1)]  # вершины нумеруются с 1

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)  # ребро u-v
    adj[v].append(u)  # ребро v-u (неориентированный)

# список для посещали или нет
visited = [False] * (n + 1)
components = []

#Запускаем BFS из каждой непосещённой вершины
for i in range(1, n + 1):
    if not visited[i]:
        # не посещали, тогда новая компонента
        component = []
        queue = deque([i])
        visited[i] = True

        while queue:
            v = queue.popleft()
            component.append(v)

            for u in adj[v]:# идем по соседям
                if not visited[u]:
                    visited[u] = True
                    queue.append(u)

        components.append(component)

# Вывод результатов
print(len(components))
for comp in components:
    print(len(comp))
    print(' '.join(map(str, comp)))