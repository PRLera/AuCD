#include <iostream>
using namespace std;

// Функция слияния двух отсортированных частей
void merge(int A[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    
    // Создаём временные массивы
    int* L = new int[n1];
    int* R = new int[n2];
    
    // Копируем данные во временные массивы
    for (int i = 0; i < n1; i++)
        L[i] = A[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = A[mid + 1 + j];
    
    // Сливаем временные массивы обратно в A
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            A[k] = L[i];
            i++;
        } else {
            A[k] = R[j];
            j++;
        }
        k++;
    }
    
    // Копируем оставшиеся элементы
    while (i < n1) {
        A[k] = L[i];
        i++;
        k++;
    }
    while (j < n2) {
        A[k] = R[j];
        j++;
        k++;
    }
    
    delete[] L;
    delete[] R;
}

// Функция сортировки слиянием
void mergeSort(int A[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(A, left, mid);
        mergeSort(A, mid + 1, right);
        merge(A, left, mid, right);
    }
}

int main() {
    int n;
    cin >> n;
    int* A = new int[n];
    
    for (int i = 0; i < n; i++)
        cin >> A[i];
    
    mergeSort(A, 0, n - 1);
    
    for (int i = 0; i < n; i++)
        cout << A[i] << " ";
    
    delete[] A;
    return 0;
}