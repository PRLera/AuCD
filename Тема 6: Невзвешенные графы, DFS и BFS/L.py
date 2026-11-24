# из связанного графа получить основное дерево(прохоже на Н)
from collections import deque

# Читаем количество вершин и рёбер
n, m = map(int, input().split())

# Создаём список смежности
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

# BFS для построения остовного дерева
visited = [False] * (n + 1)
parent_edge = [None] * (n + 1)  #для каждой вершины: ребро, которым пришли в вершину

queue = deque([1])
visited[1] = True

while queue:
    v = queue.popleft()
    for u in adj[v]:
        if not visited[u]:
            visited[u] = True
            parent_edge[u] = (v, u)  # запоминаем ребро
            queue.append(u)

# Выводим рёбра дерева (N-1)
for i in range(2, n + 1):
    print(parent_edge[i][0], parent_edge[i][1])