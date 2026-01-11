# Amir Mukhtarov, mukhtarov.amir.a@gmail.com
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0

        n = len(grid)
        m = len(grid[0])

        j = 0
        i = n - 1
        while (i >= 0) and (j < m):
            if (grid[i][j] < 0):
                res += m - j
                i -= 1
            else:
                j += 1

        return res


if __name__ == "__main__":
    grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    for row in grid:
        print(row)
    s = Solution()
    print(s.countNegatives(grid))
