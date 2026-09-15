#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int* A = new int[n];
    
    for (int i = 0; i < n; i++)
        cin >> A[i];
    
    int swaps = 0;
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (A[j] > A[j + 1]) {
                int x = A[j];
                A[j] = A[j + 1];
                A[j + 1] = x;
                swaps++;
            }
        }
    }
    
    cout << swaps << endl;
    delete[] A;
    return 0;
}