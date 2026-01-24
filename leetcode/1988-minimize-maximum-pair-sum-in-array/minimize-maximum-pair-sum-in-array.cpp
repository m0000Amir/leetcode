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
    int minPairSum(vector<int>& nums) {
        int maxSum = 0;

        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size() / 2; i++) {
          maxSum = max(maxSum, nums[i] + nums[nums.size() - 1- i]);
        }

        return maxSum;
    }
};


int main(){ 
  vector<int> nums = {3,5,4,2,4,6};
  Solution s;
  cout << s.minPairSum(nums) << endl;

  return 0;
}
