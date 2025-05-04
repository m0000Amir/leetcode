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
    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
      int res = 0;
      vector<int> num(100);

      for (auto& i : dominoes) {
        int val;
        if (i[0] < i[1]) {
          val = 10 * i[0] + i[1];
        } else {
          val = 10 * i[1] + i[0];
        }
        res += num[val];
        num[val]++;
      }

      return res;
    }
};


int main(){ 
  vector<vector<int>> dominos = {{1,2},{1,2},{1,1},{1,2},{2,2}};
  Solution s = Solution();
  cout << s.numEquivDominoPairs(dominos);

  return 0;
}
