import sys
from typing import List

def main():
    n_row, n_col = input().split()
    n_row = int(n_row)
    n_col = int(n_col)
    mem = [[-1] * n_col for _ in range(n_row)]
    mem[n_row-1][n_col-1] = 1
    print(solve(n_row, n_col, 0, 0, mem))


def solve(n_row: int, n_col: int, i: int, j: int, mem: List[List[int]]) -> int:
    if 0 <= i < n_row and 0 <= j < n_col:
        if mem[i][j] < 0:
            ans = 0
            if i < n_row-2 and j < n_col-1:
                ans += solve(n_row, n_col, i+2, j+1, mem)
            if i < n_row-1 and j < n_col-2:
                ans += solve(n_row, n_col, i+1, j+2, mem)
            mem[i][j] = ans
        return mem[i][j]
    else:
        return 0



if __name__ == '__main__':
  main()
