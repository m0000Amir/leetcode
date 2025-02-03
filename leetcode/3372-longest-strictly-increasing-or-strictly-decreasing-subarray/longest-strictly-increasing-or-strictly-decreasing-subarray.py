# Amir Mukhtarov, mukhtarov.amir.a@gmail.com
from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = 1
        dec = 1
        longest = 1

        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                inc += 1
                dec = 1
            elif nums[i + 1] < nums[i]:
                inc = 1
                dec += 1
            else:
                inc = dec = 1

            longest = max(longest, inc, dec)

        return longest


if __name__ == '__main__':
    nums = [1, 4, 3, 3, 2]
    nums = [3, 2, 1]
    s = Solution()
    print(s.longestMonotonicSubarray(nums))
