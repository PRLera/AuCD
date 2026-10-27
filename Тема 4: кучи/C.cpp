#include <iostream>
#include <vector>
#include <string>
using namespace std;

class MinHeap {
private:
    vector<int> data;  // массив для хранения кучи

    // Всплытие элемента с позиции i вверх
    void sift_up(int i) {
        while (i > 0) {
            int parent = (i - 1) / 2;  // индекс родителя
            if (data[i] < data[parent]) {
                // Если элемент меньше родителя — меняем местами
                swap(data[i], data[parent]);
                i = parent;  // продолжаем всплывать
            } else {
                break;  // элемент на своём месте
            }
        }
    }

    // Просеивание элемента с позиции i вниз
    void sift_down(int i) {
        int n = data.size();
        while (true) {
            int smallest = i;  // считаем текущий элемент наименьшим
            int left = 2 * i + 1;   // левый потомок
            int right = 2 * i + 2;  // правый потомок

            // Если левый потомок существует и меньше текущего наименьшего
            if (left < n && data[left] < data[smallest]) {
                smallest = left;
            }
            // Если правый потомок существует и меньше текущего наименьшего
            if (right < n && data[right] < data[smallest]) {
                smallest = right;
            }

            // Если наименьший — не текущий элемент, меняем местами
            if (smallest != i) {
                swap(data[i], data[smallest]);
                i = smallest;  // продолжаем просеивать
            } else {
                break;  // элемент на своём месте
            }
        }
    }

public:
    // Очистить кучу
    void clear() {
        data.clear();
    }

    // Добавить число n в кучу
    void add(int n) {
        data.push_back(n);  // кладём в конец
        sift_up(data.size() - 1);  // всплываем на правильное место
    }

    // Извлечь минимальное значение
    // Возвращает true если успешно, false если куча пуста
    bool extract(int &min_val) {
        if (data.empty()) {
            return false;  // куча пуста
        }
        min_val = data[0];  // минимум всегда в корне
        data[0] = data.back();  // переносим последний элемент на место корня
        data.pop_back();  // удаляем последний
        if (!data.empty()) {
            sift_down(0);  // просеиваем новый корень вниз
        }
        return true;
    }
};

int main() {
    MinHeap heap;
    string command;

    while (cin >> command) {
        if (command == "CLEAR") {
            heap.clear();
        } else if (command == "ADD") {
            int n;
            cin >> n;
            heap.add(n);
        } else if (command == "EXTRACT") {
            int min_val;
            if (heap.extract(min_val)) {
                cout << min_val << endl;
            } else {
                cout << "CANNOT" << endl;
            }
        }
    }

    return 0;
}