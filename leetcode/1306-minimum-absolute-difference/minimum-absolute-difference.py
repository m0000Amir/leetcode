# Amir Mukhtarov, mukhtarov.amir.a@gmail.com
from typing import List


class Solution:
    def minimumAbsDifference(self, nums: List[int]) -> List[List[int]]:
        # sort
        nums.sort()

        min_nums = []

        _min = 100_000

        for i in range(len(nums) - 1):
            _min = min(_min, abs(nums[i + 1] - nums[i]))

        for i in range(len(nums) - 1):
            if abs(nums[i + 1] - nums[i]) == _min:
                min_nums.append([nums[i], nums[i + 1]])

        return min_nums


if __name__ == "__main__":
    nums = [3, 8, -10, 23, 19, -4, -14, 27]
    s = Solution()
    print(s.minimumAbsDifference(nums))
