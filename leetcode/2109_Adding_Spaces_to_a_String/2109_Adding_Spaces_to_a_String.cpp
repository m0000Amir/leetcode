#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
  string addSpaces(string s, vector<int>& spaces) {
    string result;

    int spaceIndex = 0;
    for (int sIndex = 0; sIndex < s.size(); ++sIndex) {
      if (spaceIndex < spaces.size() && sIndex == spaces[spaceIndex]) {
        result += ' ';
        spaceIndex++;
      }
      result += s[sIndex];
    }

    return result;  
  }
};

int main(){
  string s = "LeetcodeHelpsMeLearn";
  vector<int> spaces = {8, 13, 15};

  string s2 = "spacing";
  vector<int> spaces2 = {0,1,2,3,4,5,6};

  string s3 = "icodeinpython";
  vector<int> spaces3 = {1,5,7,9};

  Solution ss;
  cout << ss.addSpaces(s3, spaces3);


  
  return 0;
}