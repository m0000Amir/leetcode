# Amir Mukhtarov, mukhtarov.amir.a@gmail.com
from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        max_sum = 0

        # sort from min to max
        nums.sort()

        for i in range(len(nums) // 2):
            max_sum = max(max_sum, nums[i] + nums[-1 - i])

        return max_sum


if __name__ == "__main__":
    nums = [3, 5, 4, 2, 4, 6]

    s = Solution()
    print(s.minPairSum(nums))
