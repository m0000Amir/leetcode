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
    int jump(vector<int>& nums) {
      int jumps = 0;
      int farthest = 0;
      int current_end = 0;

      for (int i = 0; i < nums.size() - 1; i++) {
        farthest = max(farthest, i + nums[i]);
        if (i == current_end) {
          jumps++;
          current_end = farthest;

          if (current_end >= nums.size() - 1) {
            break;
          }
        }
      }

      return jumps;
    }
};


int main(){ 
  vector<int> nums = {2,3,0,1,4};

  Solution s = Solution();
  
  cout << s.jump(nums) << endl;

  return 0;
}
