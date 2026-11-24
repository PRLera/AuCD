#полный граф = все пары соединены

# Читаем количество вершин и рёбер
n, m = map(int, input().split())

# Считаем количество уникальных рёбер
edges = set()

for _ in range(m):
    u, v = map(int, input().split())
    # Для неориентированного графа ребро (u,v) = (v,u)
    # Сохраняем в виде меньший, больший
    edge = (min(u, v), max(u, v))
    edges.add(edge)

# Для полного графа n*(n-1)/2 рёбер
required_edges = n * (n - 1) // 2

# Проверка
if len(edges) == required_edges:
    print("YES")
else:
    print("NO")