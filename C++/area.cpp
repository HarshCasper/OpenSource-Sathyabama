
#include <iostream>
using namespace std;

class Rectangle 
 {
 int width, height;
 public:
Rectangle(int x,int y);
    int area()
     {
     return width*height;
     }
};

Rectangle::Rectangle (int x, int y)
{
  width = x;
  height = y;
}

int main ()
 {

  Rectangle rect1(3,4);
  Rectangle rect2(30,23);
cout<< "\narea of first rect: " << rect1.area();
cout<< "\narea of second rect: " << rect2.area();
return 0;
}
