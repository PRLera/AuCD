from functools import cmp_to_key
import sys

# Читаем ВСЕ строки из входных данных
lines = sys.stdin.read().strip().split()

# Функция сравнения: сортируем так, чтобы получить максимальное число
def compare(a, b):
    if a + b > b + a:
        return -1  # a идет перед b
    elif a + b < b + a:
        return 1   # b идет перед a
    else:
        return 0

# Сортируем
lines.sort(key=cmp_to_key(compare))

# Выводим результат
print(''.join(lines))