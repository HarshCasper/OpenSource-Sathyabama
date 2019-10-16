#include <iostream.h>

using namespace std;
class base {
  public:
    virtual void display() {
      cout << "Parent Class" << endl;
    }
};
class swap: public base {
  int a, b, c;
  public:
    void getdata() {
      cout << "Enter the values of a and b:";
      cin >> a >> b;
    }
  void display() {
    c = a;
    a = b;
    b = c;
    cout << "A=" << a << endl << "B=" << b << endl;
  }
};
int main() {
  base * ob;
  swap bp;
  ob = & bp;
  bp.getdata();
  ob - > display();
  return 0;
}
