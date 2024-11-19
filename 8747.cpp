#include <iostream>
using namespace std;

int main() {
    long long k; // k böyük ola bilər, buna görə long long istifadə edirik
    cin >> k;

    long long n = 1;
    long long remainder = 1; // S % k başlanğıc dəyəri

    while (remainder != 0) {
        n++;
        remainder = (remainder + n) % k; // Qalıq üzərində işləyirik
    }

    cout << n << endl;
    return 0;
}