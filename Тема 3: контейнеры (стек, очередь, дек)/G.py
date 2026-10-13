n = int(input())
a = list(map(int, input().split()))

stack = []  # тупик (стек)
next_expected = 1  # следующий вагон, который должен выехать на путь 2
possible = True  # можно ли отсортировать

for wagon in a:
    # Сначала пытаемся вывести из тупика всё, что можно
    while stack and stack[-1] == next_expected:
        stack.pop()
        next_expected += 1

    # Если текущий вагон — тот, что нужен, отправляем сразу на путь 2
    if wagon == next_expected:
        next_expected += 1
    # Иначе кладём в тупик
    else:
        # Если в тупике уже есть вагон с меньшим номером — сортировка невозможна
        if stack and stack[-1] < wagon:
            possible = False
            break
        stack.append(wagon)

# В конце пытаемся вывести остатки из тупика
while stack and stack[-1] == next_expected:
    stack.pop()
    next_expected += 1

# Если все вагоны выведены — YES, иначе NO
if next_expected == n + 1:
    print('YES')
else:
    print('NO')