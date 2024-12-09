#include <iostream>

using namespace std;

class Solution {
private:
  bool binarySearch(int start, int end, vector<int>& violatingIndices) {
    int left = 0;
    int right = violatingIndices.size() - 1;

    while (left <= right) {
      int mid = left + (right - left) / 2;
      int ind = violatingIndices[mid];

      if (ind < start) {
        left = mid + 1;
      } else if (ind > end){
        right = mid - 1;
      } else {
        return true;
      }
    }
    return false;
  }

public:
    vector<bool> isArraySpecial(
      vector<int>& nums, 
      vector<vector<int>>& queries
    ) {
      vector<bool> ans;

      vector<int> violatingIndices;

      for (int i = 1; i < nums.size(); i++) {
        if (nums[i] % 2 == nums[i-1] % 2) {
          // then violate index
          violatingIndices.push_back(i);
        }
      }

      // for (int j = 0; j < violatingIndices.size(); j++) {
      //   cout << violatingIndices[j] << ' ' << endl;
      // }

      for (auto& query: queries) {
        int start = query[0];
        int end = query[1];

        if (binarySearch(start + 1, end, violatingIndices)) {
          ans.push_back(false);
        } else {
          ans.push_back(true);
        }
      }

      return ans;      
    }

};

int main(){
  vector<int> nums = {3,4,1,5,2,6};
  vector<vector<int>> queries = {{0, 4}};

  Solution s;
  vector<bool> res = s.isArraySpecial(nums=nums, queries=queries); 

  for (const auto& rr : res) {
    cout << rr << ' ' << endl;
  }

  
  return 0;
}