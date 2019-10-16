#include <iostream>

using namespace std;
class complex {
  int real, img;
  public:
    void getvalue() {
      cout << "Enter the real and imaginary value of the Complex Number: " << endl;
      cin >> real >> img;
    }
  complex operator + (complex ob) {
    complex t;
    t.real = real + ob.real;
    t.img = img + ob.img;
    return t;
  }
  void display() {
    cout << real << "+" << img << "i" << "\n";
  }
};
void main() {
  complex obj1, obj2, result;
  obj1.getvalue();
  obj2.getvalue();
  result = obj1 + obj2;
  cout << "Input Values: \n";
  obj1.display();
  obj2.display();
  cout << "Final Result: \n";
  result.display();

}
