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
    int removeDuplicates(vector<int>& nums) {
        int res = 1;

        for (int i = 1; i < nums.size(); i++) {
          if (nums[i] != nums[i - 1]) {
            nums[res] = nums[i];
            res++;
          }
        }

        return res;
    }
};


int main(){ 
  vector<int> nums = {0,0,1,1,1,2,2,3,3,4};

  Solution s;

  cout << s.removeDuplicates(nums) << endl;
  return 0;
}
