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
private:
  static bool compareInterval(vector<int> & a, vector<int> & b) {
    if (a[0] != b[0]) {
      return a[0] < b[0];
    } else {
      return a[1] > b[1];
    }
  }
public:
  int removeCoveredIntervals(vector<vector<int>>& intervals) {
      sort(intervals.begin(), intervals.end(), compareInterval);

      int k = 0;
      int maxB = -1;

      for (int i = 0; i < intervals.size(); i++) {
        if (intervals[i][1] > maxB) {
          maxB = intervals[i][1];
          k = k + 1;
        }
      }

      return k;
  }
};


int main(){ 
  vector<vector<int>> intervals = {{1, 4}, {3, 6}, {2, 8}};
  Solution s = Solution();
  cout << s.removeCoveredIntervals(intervals) << endl;

  return 0;
}
