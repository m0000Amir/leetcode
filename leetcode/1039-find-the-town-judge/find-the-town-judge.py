# Amir Mukhtarov, mukhtarov.amir.a@gmail.com
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = [0] * n

        for (a, b) in trust:
            trusted[a - 1] -= 1
            trusted[b - 1] += 1

        for i in range(len(trusted)):
            if trusted[i] == n - 1:
                return i + 1
        return -1


if __name__ == "__main__":
    n = 3
    trust = [[1, 3], [2, 3]]
    s = Solution()
    print(s.findJudge(n, trust))
