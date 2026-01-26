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
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
      int _min = INT_MAX;    

      vector<vector<int>> min_arr;

      sort(arr.begin(), arr.end());

      for (int i = 0; i < arr.size() - 1; i++ ) {
        _min = min(_min, abs(arr[i] - arr[i + 1]));
      }

      for (int i = 0; i < arr.size() - 1; i++ ) {
        if (abs(arr[i] - arr[i + 1]) == _min) {
            min_arr.push_back({arr[i], arr[i + 1]});
        }
      }

      return min_arr;
    }
};


int main(){ 
  vector<int> arr = {3,8,-10,23,19,-4,-14,27};

  Solution s;
  vector<vector<int>> res = s.minimumAbsDifference(arr);
  
  for (auto &el: res) {
    cout << "[" << el[0] << ", " << el[1] <<"], ";
  }
  cout << "]" << endl;
  return 0;
}
