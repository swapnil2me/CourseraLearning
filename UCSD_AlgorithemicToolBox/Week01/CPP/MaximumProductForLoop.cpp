#include <iostream>
#include <vector>

using std::vector;
using std::cin;
using std::cout;

long long MaxPairwiseProduct(const vector<int>& numbers){
  long long result = 0; // int will cause integer overflow, change to long long
  int n = numbers.size();
  for (int i = 0; i < n; ++i) {
    for (int j = i+1; j < n; ++j) {
      if (((long long)numbers[i])*numbers[j] > result) {
        result = ((long long)numbers[i])*numbers[j];
        // cout << result << '\n';
      }
    }
  }
  return result;
}

int main() {
  int n;
  cin >> n;
  vector<int> numbers(n);
  for (int i = 0; i < n; i++) {
    cin >> numbers[i];
  }
  // cout << numbers[0] << '\n';
  long long result = MaxPairwiseProduct(numbers);
  cout << result << '\n';
  return 0;
}
