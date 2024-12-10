#include <iostream>
#include <map>

using namespace std;

class Solution {
public:
  int maximumLength(string s) {
      map<pair<char, int>, int> count;

      for (int start = 0; start < s.size(); start++) { 
        int letterCount = 0;
        char letter = s[start];
        for (int end = start; end < s.size(); end++) {
            
            if (letter == s[end]) {
              letterCount++;
              count[{letter, letterCount}]++;
            } else {
              break;
            }
        }
      }

      int ans = 0;
      for (auto i : count) {
        // cout << i.first.first << " " << i.first.second << " " << i.second << endl;
        int len = i.first.second;
        if (i.second >=3 && ans < len)  ans = len;
        

      }

      if (ans == 0) return -1;
      return ans;
  }

};

int main(){
  string s = "aaaa";

  Solution so;

  cout << so.maximumLength(s);
  
  return 0;
}