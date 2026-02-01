# Amir Mukhtarov, mukhtarov.amir.a@gmail.com
from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        min1 = float('inf')
        min2 = float('inf')

        for num in nums[1:]:
            if num < min1:
                min2 = min1
                min1 = num

            elif num < min2:
                min2 = num

        return nums[0] + min1 + min2


if __name__ == '__main__':
    nums = [10, 3, 1, 1]

    s = Solution()
    print(s.minimumCost(nums))
