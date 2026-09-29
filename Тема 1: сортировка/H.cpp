#include <iostream>
#include <cmath>
using namespace std;

struct Point {
    int x, y;
};

double distance(Point p) {
    return sqrt(p.x * p.x + p.y * p.y);
}

void BubbleSort(Point A[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (distance(A[j]) > distance(A[j + 1])) {
                Point temp = A[j];
                A[j] = A[j + 1];
                A[j + 1] = temp;
            }
        }
    }
}

int main() {
    int n;
    cin >> n;
    
    Point* A = new Point[n];
    for (int i = 0; i < n; i++) {
        cin >> A[i].x >> A[i].y;
    }
    
    BubbleSort(A, n);
    
    for (int i = 0; i < n; i++) {
        cout << A[i].x << " " << A[i].y << endl;
    }
    
    delete[] A;
    return 0;
