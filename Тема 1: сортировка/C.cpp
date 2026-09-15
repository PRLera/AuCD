#include <iostream>
using namespace std;

void BubbleSort(int A[], int n) {
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - i - 1; j++)
            if (A[j] < A[j + 1]) {
                int x = A[j];
                A[j] = A[j + 1];
                A[j + 1] = x;
            }
}

int main() {
    int A[1000];
    int n = 0;
    
    while (cin >> A[n]) {
        n++;
    }
    
    BubbleSort(A, n);
    
    for (int i = 0; i < n; i++)
        cout << A[i] << " ";
    
    return 0;
}