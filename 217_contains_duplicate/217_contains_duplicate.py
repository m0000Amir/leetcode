from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate = set([])
        for num in nums:
            if (num in duplicate):
                return True
            duplicate.add(num)
        
        return False


if __name__ == "__main__":
    nums = [1,1,1,3,3,4,3,2,4,2] 
    sol = Solution().containsDuplicate(nums)
    print(sol)
