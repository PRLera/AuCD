import heapq

n = int(input())
aquariums = []
for i in range(n):
    f = int(input())
    aquariums.append(f)


# Функция для вычисления времени до рождения рыбки
def time_to_birth(f):
    return max(1000 - f, 1)


# Куча: (время рождения, индекс аквариума)
heap = []
for i in range(n):
    t = time_to_birth(aquariums[i])
    heapq.heappush(heap, (t, i))

# Симуляция
current_time = 0
current_position = 0  # Игорь начинает у первого аквариума (индекс 0)

while heap:
    birth_time, aquarium_idx = heapq.heappop(heap)

    # Время, за которое Игорь дойдёт до этого аквариума
    travel_time = abs(aquarium_idx - current_position)
    arrival_time = current_time + travel_time

    # Если Игорь не успевает к моменту рождения
    if arrival_time > birth_time:
        print(birth_time)
        break

    # Игорь фиксирует рождение
    current_time = birth_time
    current_position = aquarium_idx

    # Вычисляем время до следующего рождения в этом аквариуме
    aquariums[aquarium_idx] += 1
    next_birth_time = birth_time + time_to_birth(aquariums[aquarium_idx])

    heapq.heappush(heap, (next_birth_time, aquarium_idx))