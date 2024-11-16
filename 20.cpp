#include <iostream>
using namespace std;

int main() {
    int a, say = 0;
    cin >> a;

    while (true) {
        say++;
        int a1 = a, cem = 0;

        // Rəqəmlərin cəmini tapırıq
        while (a != 0) {
            cem += a % 10;
            a /= 10;
        }

        int ferq = a1 - cem;
        if (ferq <= 0) {
            cout << say << endl;
            break;
        } else {
            a = ferq;
        }
    }

    return 0;
}
