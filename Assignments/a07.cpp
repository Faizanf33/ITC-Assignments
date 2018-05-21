#include<iostream>
#include <string>

using namespace std;

double rectangle() {
  double height, width;

  cout << "Enter the length of the rectangle: ";
  cin >> height;

  cout << "Enter the width of the rectangle: ";
  cin >> width;

  cout << "Perimeter of the rectangle = " << (2 * (height + width)) << endl;
  cout << "Area of the rectangle = " << (height * width) << endl;
}

double circle() {
  double radius;
  float PI = 3.1416;

  cout << "Enter the radius of the circle: ";
  cin >> radius;

  cout << "Area of the circle = " << (PI * (radius * radius)) << endl;
  //  Circumference = 2*pi*r instead of 2*pi*r^2
  cout << "Circumference of the circle = " << (2 * PI * radius) << endl;
}


double cylinder() {
  float PI = 3.1416;
  double height, radius;

  cout << "Enter the height of the cylinder: ";
  cin >> height;

  cout << "Enter the radius of the base of the cylinder: ";
  cin >> radius;

  cout << "Volume of the cylinder = " << (PI * (radius *radius) * height) << endl;
  cout << "Surface area of the cylinder = "<< (2 * ((PI * radius * height) + (PI * (radius * radius)))) << endl;


}
int main() {
  string shape;

  cout << "Enter the shape type: (rectangle, circle, cylinder) " ;
  cin >> shape;
  cout <<'\n';

  if (shape == "1" || shape == "rectangle") rectangle();

  else if (shape == "2" || shape == "circle") circle();

  else if (shape == "3" || shape == "cylinder") cylinder();

  else cout << "Wrong option: "<< "'" << shape << "'!" << endl;

  return 0;
}
