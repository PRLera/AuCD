#include <iostream>
using namespace std;

void SelectionSort(int A[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int max_idx = i;  // индекс максимального элемента
        for (int j = i + 1; j < n; j++) {
            if (A[j] > A[max_idx]) {  // ищем максимум
                max_idx = j;
            }
        }
        // меняем местами
        int temp = A[i];
        A[i] = A[max_idx];
        A[max_idx] = temp;
    }
}

int main() {
    int A[1000];  // массив с запасом
    int n = 0;    // количество элементов
    
    // читаем все числа из входного потока
    while (cin >> A[n]) {
        n++;
    }
    
    SelectionSort(A, n);
    
    for (int i = 0; i < n; i++) {
        cout << A[i] << " ";
    }
    
    return 0;
}