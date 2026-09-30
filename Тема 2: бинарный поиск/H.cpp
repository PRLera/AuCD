#include <iostream>
using namespace std;

int main() {
    long long w, h, n;
    cin >> w >> h >> n;
    
    // Бинарный поиск по размеру стороны доски
    long long left = 0;                    // минимальный размер
    long long right = max(w, h) * n;       // максимальный размер (худший случай)
    
    while (left < right) {
        long long mid = (left + right) / 2; 
        
        // Сколько дипломов поместится на доске mid × mid
        long long count = (mid / w) * (mid / h);
        
        if (count >= n) {
            right = mid;      // хватает — пробуем меньше
        } else {
            left = mid + 1;   // не хватает — нужно больше
        }
    }
    
    cout << left << endl;
    return 0;
}
