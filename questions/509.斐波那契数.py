#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#
from functools import lru_cache
# @lc code=start


class Solution:
    def __init__(self):
        super().__init__()
        self.constants = [[1, 1], [1, 0]]

    @lru_cache(None)
    def reversion(self, N: int) -> int:
        if N < 2:
            return self.fub(N-1)+self.fib(N-2)

    def matrix_pow(self, N: int) -> int:
        """矩阵法
        """
        def multiply(A: list, B: list):
            x = A[0][0] * B[0][0] + A[0][1] * B[1][0]
            y = A[0][0] * B[0][1] + A[0][1] * B[1][1]
            z = A[1][0] * B[0][0] + A[1][1] * B[1][0]
            w = A[1][0] * B[0][1] + A[1][1] * B[1][1]

            A[0][0] = x
            A[0][1] = y
            A[1][0] = z
            A[1][1] = w

        def matrix_power(A: list, N: int):
            if (N <= 1):
                return A
            matrix_power(A, N//2)
            multiply(A, A)
            B = self.constants
            if (N % 2 != 0):
                multiply(A, B)
        if (N <= 1):
            return N
        A = self.constants
        matrix_power(A, N-1)
        return A[0][0]

    def the_Golden_Ratio(self, N: int) -> int:
        # 根据黄金分割比生成斐波那契
        golden_ratio = (1 + 5 ** 0.5) / 2
        return int((golden_ratio ** N + 1) / 5 ** 0.5)

    @lru_cache(None)
    def fib(self, N: int) -> int:
        return {
            1: lambda N: self.matrix_pow(N),
            2: lambda N: self.reversion(N),
            3: lambda N: self.the_Golden_Ratio(N)
        }[3](N)


# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.fib(2))
