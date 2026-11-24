# Читаем размер матрицы
n = int(input())

# Читаем матрицу построчно
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# считаем, что матрица корректна
ok = True

for i in range(n):
    for j in range(n):
        # Условие 1: симметричность
        if matrix[i][j] != matrix[j][i]:
            ok = False
        # Условие 2: нет петель на диагонали
        if i == j and matrix[i][j] != 0:
            ok = False

# Выводим результат
if ok:
    print("YES")
else:
    print("NO")