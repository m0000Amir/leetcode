# Amir Mukhtarov, mukhtarov.amir.a@gmail.com
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        high = len(letters)

        while low < high:
            mid = low + (high - low) // 2
            if letters[mid] <= target:
                low = mid + 1
            else:
                high = mid

        if low == len(letters):
            return letters[0]
        return letters[low]


if __name__ == "__main__":
    letters = ["c", "f", "j"]
    target = "c"

    s = Solution()
    print(s.nextGreatestLetter(letters, target))
