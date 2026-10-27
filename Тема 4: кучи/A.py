class Heap:
    def __init__(self):
        self.data = []  # список для хранения кучи

    def insert(self, k):
        """Добавить число k в кучу"""
        self.data.append(k)  # кладём в конец
        self._sift_up(len(self.data) - 1)  # "всплываем" на правильное место

    def extract(self):
        """Достать и удалить максимальный элемент"""
        max_val = self.data[0]  # максимум — в корне (индекс 0)
        # Переносим последний элемент на место корня
        self.data[0] = self.data[-1]
        self.data.pop()  # удаляем последний
        if self.data:  # если куча не пуста
            self._sift_down(0)  # "просеиваем вниз"
        return max_val

    def _sift_up(self, i):
        """Всплытие элемента на позицию i"""
        while i > 0:
            parent = (i - 1) // 2  # индекс родителя
            if self.data[i] > self.data[parent]:
                # Если элемент больше родителя — меняем местами
                self.data[i], self.data[parent] = self.data[parent], self.data[i]
                i = parent  # продолжаем всплывать
            else:
                break  # элемент на своём месте

    def _sift_down(self, i):
        """Просеивание элемента с позиции i вниз"""
        n = len(self.data)
        while True:
            largest = i  # считаем, что наибольший — текущий
            left = 2 * i + 1   # левый потомок
            right = 2 * i + 2  # правый потомок

            # Если левый потомок существует и больше текущего наибольшего
            if left < n and self.data[left] > self.data[largest]:
                largest = left
            # Если правый потомок существует и больше текущего наибольшего
            if right < n and self.data[right] > self.data[largest]:
                largest = right

            # Если наибольший — не текущий элемент, меняем местами
            if largest != i:
                self.data[i], self.data[largest] = self.data[largest], self.data[i]
                i = largest  # продолжаем просеивать
            else:
                break  # элемент на своём месте


#  Основная программа
n = int(input())
heap = Heap()

for _ in range(n):
    command = input().split()
    if command[0] == '0':
        # Команда Insert
        k = int(command[1])
        heap.insert(k)
    else:
        # Команда Extract
        print(heap.extract())