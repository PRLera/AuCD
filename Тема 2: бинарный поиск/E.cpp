#include <iostream>
using namespace std;

// Функция проверки: можно ли расставить K коров с расстоянием >= distance
bool canPlace(int stalls[], int N, int K, int distance) {
    int cows = 1;              // первую корову ставим в первое стойло
    int last = stalls[0];      // позиция последней коровы
    
    for (int i = 1; i < N; i++) {           // проходим по всем стойлам
        if (stalls[i] - last >= distance) { // если расстояние достаточно
            cows++;                         // ставим корову
            last = stalls[i];               // запоминаем позицию
            
            if (cows == K) return true;     // всех расставили!
        }
    }
    
    return false;  // не хватило стойл
}

int main() {
    int N, K;
    cin >> N >> K;
    
    int stalls[N];
    for (int i = 0; i < N; i++) {
        cin >> stalls[i];
    }
    
    // Бинарный поиск по ответу
    int left = 0;
    int right = stalls[N-1] - stalls[0];
    int answer = 0;
    
    while (left <= right) {
        int mid = (left + right) / 2;
        
        if (canPlace(stalls, N, K, mid)) {
            answer = mid;       // запоминаем ответ
            left = mid + 1;     // пробуем больше
        } else {
            right = mid - 1;    // пробуем меньше
        }
    }
    
    cout << answer << endl;
    return 0;
}