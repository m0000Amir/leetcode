// Amir Mukhtarov, mukhtarov.amir.a@gmail.com
#include <iostream> 
#include <vector> 
#include <string> 
#include <algorithm> 
#include <unordered_map> 
#include <map> 
#include <unordered_set> 
#include <set> 
#include <queue> 
#include <stack> 
#include <deque> 
#include <cmath> 
#include <limits> 

using namespace std; 
 
class Solution {
  
public:
  vector<int> dp;

  Solution() {
    if (dp.empty()) {
      dp.resize(31, -1);
    }
  }

  int fib(int n) {

    if (n <= 1) {
      return n;
    }
    int first, second;

    if (dp[n - 1] == -1) {
      first = fib(n - 1);
    } else {
      first = dp[n -1];
    }

    if (dp[n - 2] == -1) {
      second = fib(n - 2);
    } else {
      second = dp[n - 2];
    }

    dp[n] = first + second;

    return first + second;
  }
};


int main(){ 

  Solution s = Solution();
  int n = 10;
  cout << s.fib(n) << endl;

  return 0;
}
