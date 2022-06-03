from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if (digits[-1] != 9):
            digits[-1] +=1
            return digits
        else:
            digits.insert(0, 0)
            for i in range(len(digits)-1, -1, -1):
                if (digits[i] == 9):
                    digits[i] = 0
                else:
                    digits[i] = digits[i] + 1
                    break
        if digits[0] == 0: return digits[1:]
        return digits



if __name__ == "__main__":
    solution = Solution()
    digits = [1,9, 9, 9, 9]
    print(solution.plusOne(digits))