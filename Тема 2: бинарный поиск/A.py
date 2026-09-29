def doubl(a, b):
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == b:
            return True
        elif a[mid] < b:
            left = mid + 1
        else:
            right = mid - 1
    return False

# Читаем N и K из первой строки
N, K = map(int, input().split())

# Читаем первый массив (N чисел)
arrN = list(map(int, input().split()))

# Читаем второй массив (K чисел)
arrK = list(map(int, input().split()))

arrN.sort()

for i in arrK:
    if doubl(arrN, i):
        print("YES")
    else:
        print("NO")