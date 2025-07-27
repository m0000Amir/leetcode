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
  int countHillValley(vector<int>& nums) {
      int count = 0;
      int left = 0;
      for (int i = 1; i < nums.size() - 1; i++) {
        if (nums[i] != nums[i + 1]) {
          if ((nums[i] > nums[left] && nums[i] > nums[i+1]) ||
              (nums[i] < nums[left] && nums[i] < nums[i+1])) {
            
            ++count;
          }
          left = i;
        }
      }
    return count;
  }
};


int main(){ 
  Solution s = Solution();

  vector<int> nums = {2, 4, 1, 1, 6, 5};

  cout << s.countHillValley(nums) << endl;

  return 0;
}
