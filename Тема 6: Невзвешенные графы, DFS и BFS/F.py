# Читаем количество вершин
n = int(input())

# Читаем матрицу смежности
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Состояния вершин: 0 = не посещена, 1 = в процессе, 2 = завершена
color = [0] * n
#есть ли цикл
has_cycle = False


def dfs(v):
    global has_cycle
    color[v] = 1  #"в процессе"

    # Проходим по всем соседям
    for u in range(n):
        if matrix[v][u] == 1:  # есть ребро v - u
            if color[u] == 1:  # вершина на текущем пути, тогда цикл
                has_cycle = True
                return
            elif color[u] == 0:  # вершина не посещена, обходим
                dfs(u)
                if has_cycle:
                    return

    color[v] = 2  #"завершена"


# Запускаем DFS из каждой непосещённой вершины
for i in range(n):
    if color[i] == 0:
        dfs(i)
        if has_cycle:
            break

# Выводим результат
if has_cycle:
    print(1)
else:
    print(0)