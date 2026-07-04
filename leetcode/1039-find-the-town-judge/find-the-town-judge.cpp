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

class Solution
{
public:
  int findJudge(int n, vector<vector<int>> &trust)
  {
    vector<int> trusted(n, 0);

    for (int i = 0; i < trust.size(); i++ ) {
      trusted[trust[i][0] - 1] -= 1;
      trusted[trust[i][1] - 1] += 1;
    }

    for (int i = 0; i < trusted.size(); i++ ) {
      if (trusted[i] == n - 1) {
        return i + 1;
      }
    }
    return -1;
  }
};

int main()
{

  cout << 1000 << endl;

  int n = 3;
  vector<vector<int>> trust = {{1, 3}, {2, 3}};

  Solution s = Solution();
  cout << s.findJudge(n, trust);

  return 0;
}
