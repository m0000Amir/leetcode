# Amir Mukhtarov, mukhtarov.amir.a@gmail.com
from typing import List


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10**9 + 7

        dp_score = [[-1] * n for _ in range(n)]
        dp_count = [[0] * n for _ in range(n)]

        dp_score[0][0] = 0
        dp_count[0][0] = 1

        prev_dirs = [(-1, 0), (0, -1), (-1, -1)]

        for i in range(n):
            for j in range(n):
                if board[i][j] == "X":
                    continue
                if i == 0 and j == 0:
                    continue

                best_prev_score = -1
                total_ways = 0

                for di, dj in prev_dirs:
                    pi, pj = i + di, j + dj
                    if 0 <= pi < n and 0 <= pj < n:
                        prev_score = dp_score[pi][pj]
                        if prev_score != -1:
                            if prev_score > best_prev_score:
                                best_prev_score = prev_score
                                total_ways = dp_count[pi][pj]
                            elif prev_score == best_prev_score:
                                total_ways = (
                                    total_ways + dp_count[pi][pj]
                                ) % MOD

                if best_prev_score != -1:
                    current_points = (
                        int(board[i][j]) if board[i][j].isdigit() else 0
                    )
                    dp_score[i][j] = best_prev_score + current_points
                    dp_count[i][j] = total_ways

        final_score = dp_score[-1][-1]
        final_count = dp_count[-1][-1]

        if final_score == -1:
            return [0, 0]

        return [final_score, final_count]


if __name__ == "__main__":
    board = ["E23", "2X2", "12S"]
    s = Solution()
    print(s.pathsWithMaxScore(board))
