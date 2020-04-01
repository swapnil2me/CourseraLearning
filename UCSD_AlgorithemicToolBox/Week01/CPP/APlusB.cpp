#include <iostream>

int main( ) {
  int a=0;
  int b=0;
  int sum=0;
  std::cin>>a;
  std::cin>>b;
  sum = a+b;
  std::cout<<sum;
  return 0;
}
// g++ -std=c++11 -Wall -Wextra -Werror APlusB.cpp -o APlusB
