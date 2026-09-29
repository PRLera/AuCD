def doubl(a,b):
    left = 0
    right= len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == b:
            return a[mid]
        elif a[mid] < b:
            left = mid + 1
        else:
            right = mid - 1

    # Проверяем краевые случаи
    # все элементы больше x
    if left == 0:
        return a[0]
    # все элементы меньше x
    if left == len(a):
        return a[-1]

    # Сравнение двух соседей
    left_v = a[left - 1]  #слева
    right_v = a[left]  #справа

    # Выбираем ближайший
    if abs(b - left_v) <= abs(b - right_v):
        return left_v
    else:
        return right_v

N,K = map(int,input().split())

arrN = list(map(int,input().split()))
arrK = list(map(int,input().split()))

arrN.sort()

for i in arrK:
    result = doubl(arrN, i)
    print(result)