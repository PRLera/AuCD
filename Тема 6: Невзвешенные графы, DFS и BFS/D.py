#Найти количество вершин в компоненте связности с заданной вершиной S
#сколько вершин достижимо из стартовой

# Читаем количество вершин и стартовую вершину
n, s = map(int, input().split())

matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

visited = [False] * n  # массив посещённых вершин

def dfs(v):
    visited[v] = True  # помечаем вершину как посещённую
    count = 1

    # Проходим по всем соседям
    for u in range(n):
        if matrix[v][u] == 1 and not visited[u]:  # есть ребро и не посещена
            count += dfs(u)  # рекурсивно обходим соседа

    return count


# DFS из вершины s (нумерация с 0)
result = dfs(s - 1)

print(result)