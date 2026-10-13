n_tests = int(input())

for _ in range(n_tests):
    data = input().split()
    k = int(data[0])
    containers = [float(x) for x in data[1:k + 1]]

    # Порядок, в котором контейнеры должны выйти (по возрастанию)
    sorted_containers = sorted(containers)

    stack = []  # склад (стек)
    next_idx = 0  # индекс следующего ожидаемого контейнера
    possible = True

    for container in containers:
        # Сначала пытаемся вывести из склада всё, что можно
        while stack and stack[-1] == sorted_containers[next_idx]:
            stack.pop()
            next_idx += 1

        # Если текущий контейнер — тот, что нужен сейчас
        if container == sorted_containers[next_idx]:
            next_idx += 1
        else:
            # Проверяем: если верх стека меньше текущего,
            # то текущий заблокирует его — невозможно
            if stack and stack[-1] < container:
                possible = False
                break
            # Иначе кладём в склад
            stack.append(container)

    # В конце пытаемся вывести остатки из склада
    while stack and stack[-1] == sorted_containers[next_idx]:
        stack.pop()
        next_idx += 1

    # Если вывели все контейнеры — возможно
    if possible and next_idx == k:
        print(1)
    else:
        print(0)