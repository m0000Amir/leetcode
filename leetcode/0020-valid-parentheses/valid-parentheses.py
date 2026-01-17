# Amir Mukhtarov, mukhtarov.amir.a@gmail.com
class Solution:
    def isValid(self, s: str) -> bool:
        h = {
            '}': '{',
            ']': '[',
            ')': '(',
        }

        stack = []

        for char in s:
            if char in h.values():
                stack.append(char)
            elif char in h:
                if not stack or stack.pop() != h[char]:
                    return False

        return len(stack) == 0


if __name__ == '__main__':
    s = "([])"
    solution = Solution()

    print(solution.isValid(s))
