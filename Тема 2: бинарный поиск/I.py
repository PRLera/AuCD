# Читаем первый массив
N = int(input())
arr1 = list(map(int, input().split()))

# Читаем второй массив
M = int(input())
arr2 = list(map(int, input().split()))

# Создаем словарь: ключ = число, значение = сколько раз встречается
count = {}
for x in arr1:
    if x in count:
        count[x] += 1
    else:
        count[x] = 1

# Для каждого элемента второго массива смотрим в словарь
result = []
for x in arr2:
    if x in count:
        result.append(count[x])
    else:
        result.append(0)

# Выводим результат
print(*result)