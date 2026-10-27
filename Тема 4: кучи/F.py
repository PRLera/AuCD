import heapq

n = int(input())
cargoes = []

for _ in range(n):
    t, l = map(int, input().split())
    cargoes.append((t, l))

# Сортируем грузы по времени прибытия
cargoes.sort()

# Куча для хранения времени освобождения аппаратов
machines = []

for t, l in cargoes:
    end_time = t + l  # когда этот груз будет обработан

    # Если есть свободный аппарат (освободился до прибытия груза)
    if machines and machines[0] <= t:
        # Используем его — заменяем время освобождения
        heapq.heapreplace(machines, end_time)
    else:
        # Нет свободного — добавляем новый аппарат
        heapq.heappush(machines, end_time)

# Количество аппаратов = размер кучи
print(len(machines))