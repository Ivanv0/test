#include <iostream>
#include <cmath>

using namespace std;

int main() {
    float a,b,c;
    cout << "Input a, b and c" << endl;
    cin >> a >> b >> c;
    if (a != 0) {
        if (b != 0) {
            if (c != 0) { // ax2+bx+c=0
                float d = pow(b,2)-4*a*c;
                if (d>0) {
                    float x1 = (-b+sqrt(d))/(2*a);
                    float x2 = (-b-sqrt(d))/(2*a);
                    cout << "x1= " << x1 << "  x2= " << x2 << endl;
                } else if (d==0) {
                    float x = -b/2*a;
                    cout << "x= " << x << endl;
                } else cout << "d<0" << endl;
            } else if (c == 0) { //ax2+bx=0
                cout << "x=0, x2=" << (-b/a) << endl;
            }
        } else if (b == 0) {
            if (c != 0) { // ax2+c=0
                float v = -c/a;
                if (v == abs(v)) {
                    cout << "x=" << sqrt(v) << endl;
                } else {
                    cout << "x doesn't exist" << endl;
                }
            } else if (c == 0) { // ax2=0
                cout << "x=0" << endl;
            }
        }
    } else if (a == 0) {
        if (b != 0) {
            if (c != 0) { // bx+c=0
                cout << "x=" << (-c/b) << endl;
            } else if (c == 0) { // bx=0
                cout << "x=0" << endl;
            }
        } else if (b == 0) {
            if (c != 0) { // c=0
                cout << "x doesn't exist" << endl;
            } else if (c == 0) { // 0=0
                cout << "any x" << endl;
            }
        }
    }
}
