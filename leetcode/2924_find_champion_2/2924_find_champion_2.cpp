#include <iostream>

using namespace std;


class Solution {
public:
  int findChampion(int n, vector<vector<int>>& edges) {
    int champion = -1;
    int championsCount = 0;

    vector<int> indegree(n, 0);

    for (vector<int> edge: edges) {
      indegree[edge[1]]++;
    }

    for (int i = 0; i < n; i++) {
      if (indegree[i] == 0) {
        champion = i;
        championsCount++;
      }
    }

    return championsCount > 1 ? -1 : champion ;
  }
};


int main() {
  int n = 3;
  vector<vector<int>> edges {
    {0, 1}, {1, 2}
  };

  Solution s;

  int res = s.findChampion(n, edges);
  
  cout << res << endl;

  return 0;
}