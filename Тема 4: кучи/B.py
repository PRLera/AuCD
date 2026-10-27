class HeapSort:
    def __init__(self, array):
        self.array = array
        self.size = len(array)

    def sift_down(self, i, heap_size):
        """Просеивание элемента с позиции i вниз"""
        while True:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < heap_size and self.array[left] > self.array[largest]:
                largest = left
            if right < heap_size and self.array[right] > self.array[largest]:
                largest = right

            if largest != i:
                self.array[i], self.array[largest] = self.array[largest], self.array[i]
                i = largest
            else:
                break

    def build_heap(self):
        """Построение max-heap из массива"""
        for i in range(self.size // 2 - 1, -1, -1):
            self.sift_down(i, self.size)

    def sort(self):
        """Пирамидальная сортировка"""
        self.build_heap()
        for i in range(self.size - 1, 0, -1):
            self.array[0], self.array[i] = self.array[i], self.array[0]
            self.sift_down(0, i)
        return self.array


# === Основная программа ===
n = int(input())
a = list(map(int, input().split()))

sorter = HeapSort(a)
result = sorter.sort()

print(*result)