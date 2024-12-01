#include <iostream>
#include <unordered_map>
#include <deque>


using namespace std;

class Solution {
public:
  vector<vector<int>> validArrangement(vector<vector<int>> &pairs) {
    unordered_map<int, deque<int>> adjacencyMatrix;
    unordered_map<int, int> inDegree, outDegree;

    // create adjeacency matrix and in-degrees, and out-degrees
    for (auto& pair : pairs) {
      int start = pair[0];
      int end = pair[1];
      adjacencyMatrix[start].push_back(end);
      outDegree[start]++;
      inDegree[end]++;
    }

    for (auto& i : adjacencyMatrix) {
      cout << i.first << ": ";
      for (int j = 0; j < i.second.size(); j++) {
        cout << i.second[j] << " ";
      }
      cout << endl;
    }

    vector<int> dfsResult;
    // lambda function to DFS traversal
    function<void(int)> visit = [&](int node) {
      while (!adjacencyMatrix[node].empty()) {
        int nextNode = adjacencyMatrix[node].front();
        adjacencyMatrix[node].pop_front();
        visit(nextNode);
      }
      dfsResult.push_back(node);
    };

    int startNode = -1;
    for (const auto& entry : outDegree) {
      int node = entry.first;
      if (outDegree[node] == 1 + inDegree[node]) {
        startNode = node;
        break;
      }
    }

    if (startNode == -1) {
      startNode = pairs[0][0];
    }

    visit(startNode);
    reverse(dfsResult.begin(), dfsResult.end());

    // construct result pairs;
    vector<vector<int>> result;
    for (int i = 1; i < dfsResult.size(); i++) {
      result.push_back({dfsResult[i - 1], dfsResult[i]});
    }

    return result;
  }

};

int main(){
  // [[5,1],[4,5],[11,9],[9,4]]
  vector<vector<int>> pairs = {
    {5, 1}, {4, 5}, {11, 9}, {9, 4}
  };
  Solution s;
  vector<vector<int>> res  = s.validArrangement(pairs);

  for (auto& pair: res) {
    cout << pair[0] << ", " << pair[1] << ", ";
  }
  cout << endl;

  return 0;
}