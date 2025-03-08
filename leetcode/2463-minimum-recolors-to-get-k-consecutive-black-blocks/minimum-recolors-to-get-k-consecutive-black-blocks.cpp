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
    int minimumRecolors(string blocks, int k) {
      int res = k;
      int recolor = 0;

      int left = 0;

      for (int right = 0; right <= blocks.size(); right++) {
        if (blocks[right] == 'W') {
          recolor++;
        }
        if (right - left + 1 == k) {
          res = min(res, recolor);
          if (blocks[left] == 'W') {
            recolor--;
          }
          left++;
        }
      }


      return res;
        
    }
};


int main(){ 
  string blocks = "WBBWWBBWBW";
  int k  = 7;

  Solution s = Solution();

  cout << s.minimumRecolors(blocks, k) << endl;

  return 0;
}
