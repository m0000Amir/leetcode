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
    bool isValid(string s) {
      stack<char> st;

      for (char c : s) {
        if (c == '{' || c == '[' || c == '(') {
          st.push(c);
        } else {
          if (st.empty()) return false;

          char top = st.top();
          st.pop();
          
          if (
            (c == ')' && top != '(') ||
            (c == '}' && top != '{') ||
            (c == ']' && top != '[')
          ) {
            return false;
          }

        }
      }
      return st.empty();
    }
};


int main(){ 
  string s = "([])";
  Solution solution;
  cout << solution.isValid(s) << endl;
  cout << "AAAAA" << endl;
  return 0;
}
