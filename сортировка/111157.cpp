#include <iostream>
using namespace std;

void InsertionSort(int A[], int n) {
    for (int i = 1; i < n; i++) {
        int key = A[i];  // элемент, который нужно вставить
        int j = i - 1;
        
        // Сдвигаем элементы вправо, пока они больше key
        while (j >= 0 && A[j] > key) {
            A[j + 1] = A[j];
            j--;
        }
        
        // Вставляем key на правильную позицию
        A[j + 1] = key;
    }
}

int main() {
    int A[1000];  // массив с запасом
    int n = 0;    // количество элементов
    
    // читаем все числа из входного потока
    while (cin >> A[n]) {
        n++;
    }
    
    InsertionSort(A, n);
    
    for (int i = 0; i < n; i++) {
        cout << A[i] << " ";
    }
    
    return 0;
}