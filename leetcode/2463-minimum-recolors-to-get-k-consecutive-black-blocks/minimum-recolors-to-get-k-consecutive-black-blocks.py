# Amir Mukhtarov, mukhtarov.amir.a@gmail.com


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = k
        recolor = 0

        left = 0

        for right in range(len(blocks)):
            if blocks[right] == 'W':
                recolor += 1
            if right - left + 1 == k:
                res = min(res, recolor)
                if blocks[left] == 'W':
                    recolor -= 1
                left += 1

        return res


if __name__ == '__main__':
    blocks = "WBBWWBBWBW"
    k = 7

    blocks = "WBWBBBW"
    k = 2

    s = Solution()
    print(s.minimumRecolors(blocks, k))
