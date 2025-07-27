# Amir Mukhtarov, mukhtarov.amir.a@gmail.com
from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        res = 0
        left = 0
        for i in range(1, len(nums) - 1):
            if nums[i] != nums[i+1]:
                if (nums[i] < nums[left] and nums[i] < nums[i+1]) or \
                   (nums[i] > nums[left] and nums[i] > nums[i+1]):
                    res += 1
                left = i
        return res


if __name__ == '__main__':
    nums = [2, 4, 1, 1, 6, 5]
    s = Solution()
    print(s.countHillValley(nums))
