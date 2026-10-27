import heapq

n = int(input())
numbers = list(map(int, input().split()))

# Создаём кучу из чисел
heapq.heapify(numbers)

total_cost = 0.0

# Пока в куче больше одного числа
while len(numbers) > 1:
    # Берём два наименьших числа
    a = heapq.heappop(numbers)
    b = heapq.heappop(numbers)

    # Складываем их
    sum_ab = a + b

    # Добавляем стоимость операции (5% от суммы)
    total_cost += sum_ab * 0.05

    # Кладём результат обратно в кучу
    heapq.heappush(numbers, sum_ab)

# Выводим результат с двумя знаками после запятой
print(f"{total_cost:.2f}")