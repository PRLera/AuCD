#для каждого ребра u-v, u идёт раньше v в перестановке(перестановка это топологическая перестановка)

# Читаем количество вершин и рёбер
n, m = map(int, input().split())

# Читаем рёбра
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

# Читаем перестановку
permutation = list(map(int, input().split()))

# словарь: позиция вершины в перестановке
position = {}
for i, v in enumerate(permutation): #позиция, вершина
    position[v] = i

# Проверяем условие топологической сортировки
is_topo = True

for u, v in edges:
    if position[u] >= position[v]:
        is_topo = False
        break

# Выводим результат
if is_topo:
    print("YES")
else:
    print("NO")