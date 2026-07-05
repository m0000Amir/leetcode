# Amir Mukhtarov, mukhtarov.amir.a@gmail.com
from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n+1)]
        for (a, b, d) in roads:
            graph[a].append((b, d))
            graph[b].append((a, d))
        
        # for i in range(1, n+1):
        #     print(f'{i} - {graph[i]}')

        min_d = float('inf')
        visited = [False] * (n + 1)

        def dfs(min_d, node):
            visited[node] = True
            for (node2, d) in graph[node]:
                min_d = min(min_d, d)
                if not visited[node2]:
                    min_d = dfs(min_d, node2)
            return min_d

        min_d = dfs(min_d, 1)
        return min_d


if __name__ == "__main__":
    n = 4
    roads = [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]
    s = Solution()
    print(s.minScore(n, roads))
