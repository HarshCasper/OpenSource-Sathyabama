#include <iostream.h>

#include <stdlib.h>

#define PI 3.14
using namespace std;
class fn {
  public:
    void area(int);
  void area(int, int);
  void area(float, int, int);
};
void fn::area(int a) {
  cout << "Area of Circle is: " << PI * a * a;
}
void fn::area(int a, int b) {
  cout << "Area of Square is: " << a * b;
}
void fn::area(float t, int a, int b) {
  cout << "Area of Triangle is: " << t * a * b;
}
int main() {
  int ch, a, b, r;
  fn ob;
  cout << "*****Function Overloading*****" << endl;
  while (1) {
    cout << endl << "1.Calculate Area of Circle\n2.Calculated Area of Square\n3.Calculate Area of Triangle\n4.Exit\n" << endl;
    cout << "Enter your choice:" << endl;
    cin >> ch;
    switch (ch) {
    case 1:
      cout << "Enter the radius of the circle:" << endl;
      cin >> r;
      ob.area(r);
      break;
    case 2:
      cout << "Enter the sides of the rectangle:" << endl;
      cin >> a >> b;
      ob.area(a, b);
      break;
    case 3:
      cout << "Enter the sides of the triangle:" << endl;
      cin >> a >> b;
      ob.area(0.5, a, b);
      break;
    case 4:
      exit(0);
    default:
      cout << "Wrong Option! Enter again!" << endl;
    }
  }
  return 0;
}
