# Amir Mukhtarov, mukhtarov.amir.a@gmail.com
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[res] = nums[i]
                res += 1
        return res


if __name__ == '__main__':
    nums = [1, 1, 2]

    s = Solution()
    print(s.removeDuplicates(nums))
