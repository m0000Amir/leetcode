#include <iostream>
#include <unordered_map>

using namespace std;

class Solution {
public:
  bool checkIfExist(vector<int>& arr) {
    unordered_map<int, int> h;

    for (int i = 0; i < arr.size(); i++) {
      h[arr[i]]++;
    }
  

    for (int i = 0; i < arr.size(); i++) {
      if (arr[i] != 0 && h.find(arr[i] * 2) != h.end()) {
        return true;
      }
      
      if (arr[i] == 0 && arr[i] > 1) {
        return true;
      }
    }
    return false;      
  }

};

int main(){
  vector<int> arr0 = {
    10, 2, 5, 3
  };

  vector<int> arr1 = {
    3, 1, 7, 11
  };

  vector<int> arr2 = {
    -2, 0, 10, -19, 4, 6, -8
  };

  Solution s;

  cout << s.checkIfExist(arr2);

  
  return 0;
}