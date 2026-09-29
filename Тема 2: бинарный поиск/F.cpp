#include <iostream>
using namespace std;

int main() {
    long long N, x, y;
    cin >> N >> x >> y;
    
    // Время на первую копию (быстрый ксерокс)
    long long first = min(x, y);
    
    // Бинарный поиск по времени после первой копии
    long long left = 0, right = N * first;
    
    while (left < right) {
        long long mid = (left + right) / 2;
        
        // Сколько копий сделаем за mid секунд после первой?
        if (1 + mid / x + mid / y >= N)
            right = mid;      // хватает — пробуем меньше
        else
            left = mid + 1;   // не хватает — нужно больше
    }
    
    // Ответ = время первой копии + найденное время
    cout << first + left << endl;
    return 0;
}