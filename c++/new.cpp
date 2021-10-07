#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int a,b,c;
    cout << "Введите a, b и c" << endl;
    cin >> a >> b >> c;
    float d = pow(b,2)-4*a*c;
    if (d>0) {
        float x1 = (-b+sqrt(d))/(2*a);
        float x2 = (-b-sqrt(d))/(2*a);
        cout << "x1= " << x1 << "  x2= " << x2 << endl;
    } else if (d==0) {
        float x = -d/2*a;
        cout << "x= " << x << endl;
    } else cout << "d<0" << endl;
}