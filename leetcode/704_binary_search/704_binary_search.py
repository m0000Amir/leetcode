from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        h = len(nums) - 1
        while (l <= h):
            i = (l + h) // 2;
            if (nums[i] == target): return i
            if (nums[i] < target):
                l = i + 1
            else:
                h = i - 1 
        return -1


if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9
    print(Solution().search(nums, target))
