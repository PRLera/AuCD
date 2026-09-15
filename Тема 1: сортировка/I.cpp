#include <iostream>
#include <string>
using namespace std;

int main() {
    string word1, word2;
    cin >> word1 >> word2;
    
    // Если длины разные - точно не анаграммы
    if (word1.length() != word2.length()) {
        cout << "NO" << endl;
        return 0;
    }
    
    // Массив для подсчета символов (26 букв + 10 цифр = 36)
    int count[36] = {0};
    
    // Считаем символы первого слова
    for (int i = 0; i < word1.length(); i++) {
        char c = word1[i];
        if (c >= 'a' && c <= 'z') {
            count[c - 'a']++;
        } else if (c >= '0' && c <= '9') {
            count[c - '0' + 26]++;
        }
    }
    
    // Вычитаем символы второго слова
    for (int i = 0; i < word2.length(); i++) {
        char c = word2[i];
        if (c >= 'a' && c <= 'z') {
            count[c - 'a']--;
        } else if (c >= '0' && c <= '9') {
            count[c - '0' + 26]--;
        }
    }
    
    // Проверяем, все ли счетчики равны 0
    bool isAnagram = true;
    for (int i = 0; i < 36; i++) {
        if (count[i] != 0) {
            isAnagram = false;
            break;
        }
    }
    
    if (isAnagram) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
    
    return 0;
}