#Исток = столбец нули (никто не входит)
#Сток = строка нули (никуда не выходит)

# Читаем количество вершин
n = int(input())

# Читаем матрицу смежности
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Находим истоки и стоки
sources = []  # истоки
sinks = []  # стоки

for i in range(n):
    # Проверяем, является ли вершина i истоком
    # Исток: в столбце i все нули (ни одно ребро не входит)
    is_source = True
    for j in range(n):
        if matrix[j][i] == 1:  # есть ребро из j в i
            is_source = False
            break
    if is_source:
        sources.append(i + 1)  # вершины нумеруются с 1

    # Проверяем, является ли вершина i стоком
    # Сток: в строке i все нули (ни одно ребро не выходит)
    is_sink = True
    for j in range(n):
        if matrix[i][j] == 1:  # есть ребро из i в j
            is_sink = False
            break
    if is_sink:
        sinks.append(i + 1)  # вершины нумеруются с 1

# Выводим результаты
print(len(sources))
print(' '.join(map(str, sources)))
print(len(sinks))
print(' '.join(map(str, sinks)))