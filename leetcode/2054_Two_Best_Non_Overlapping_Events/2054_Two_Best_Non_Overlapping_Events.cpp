#include <iostream>

using namespace std;

class Solution {
public:
    int maxTwoEvents(vector<vector<int>>& events) {
        vector<array<int, 3>> times;
        for (auto& e : events) {
            // 1 denotes start time.
            times.push_back({e[0], 1, e[2]});
            // 0 denotes end time.
            times.push_back({e[1] + 1, 0, e[2]});
        }
        int ans = 0, maxValue = 0;
        sort(begin(times), end(times));
        for (auto& timeValue : times) {
            // If current time is a start time, find maximum sum of maximum end
            // time till now.
            if (timeValue[1]) {
                ans = max(ans, timeValue[2] + maxValue);
            } else {
                maxValue = max(maxValue, timeValue[2]);
            }
        }
        return ans;
    }
};

int main(){
  vector<vector<int>> events = {
    {1, 3, 2},
    {4, 5, 2},
    {2, 4, 3}
  };

  Solution s;
  
  cout << s.maxTwoEvents(events);
  
  return 0;
}