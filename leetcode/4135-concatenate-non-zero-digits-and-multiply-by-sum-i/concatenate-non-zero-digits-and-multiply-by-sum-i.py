# Amir Mukhtarov, mukhtarov.amir.a@gmail.com
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        sum = 0
        n_str = str(n)
        non_zero_str = ""
        for i in n_str:
            if i != "0":
                non_zero_str += i
        print(non_zero_str)
        for i in non_zero_str:
            sum += int(i)

        return int(non_zero_str) * sum


if __name__ == "__main__":
    n = 10203004
    s = Solution()
    print(s.sumAndMultiply(n))
