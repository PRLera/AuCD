#include <iostream>
using namespace std;

void CountSort(int A[], int n) {
    int count[101] = {0};
    
    for (int i = 0; i < n; i++) {
        count[A[i]]++;
    }
    
    int index = 0;
    for (int num = 0; num <= 100; num++) {
        for (int j = 0; j < count[num]; j++) {
            A[index] = num;
            index++;
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    int A[200000];
    int n = 0;
    
    while (cin >> A[n]) {
        n++;
    }
    
    CountSort(A, n);
    
    for (int i = 0; i < n; i++) {
        cout << A[i] << " ";
    }
    
    return 0;
}