from collections import deque

N, K = map(int, input().split())
a = list(map(int, input().split()))

d = deque()  # дек для хранения индексов

for i in range(N):
    # Удаляем индексы, которые вышли за пределы окна
    while d and d[0] < i - K + 1:
        d.popleft()

    # Удаляем индексы элементов, которые больше текущего
    while d and a[d[-1]] >= a[i]:
        d.pop()

    # Добавляем текущий индекс
    d.append(i)

    # Выводим минимум, когда окно полностью заполнено
    if i >= K - 1:
        print(a[d[0]])