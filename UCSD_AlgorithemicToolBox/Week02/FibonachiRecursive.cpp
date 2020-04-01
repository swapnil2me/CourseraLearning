#include <iostream>
#include <cassert>

int fibonacci_naive(int n){
  if (n<=1)
    return n;

  return fibonacci_naive(n-1) + fibonacci_naive(n-2);
}

int fibonacci_fast(int n){
  int result = 0;
  int f_1 = 0;
  int f_2 = 0;
  for (int i = 0; i < n; i++) {
    // std::cout << result << '\n';
    f_2 = f_1;
    f_1 = result;
    if (i==1) {
      f_1=1;
    }
    result = f_1 + f_2;
  }

  return result;
}

int main() {
  int n = 0;
  std::cin >> n;
  std::cout << fibonacci_fast(n) << '\n';
  return 0;
}
