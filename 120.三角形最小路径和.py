#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#
from typing import List
import functools
# @lc code=start
class Solution:
    def _error(self, triangle: List[List[int]]) -> int:
        return sum([min(_) for _ in triangle])

    def recursion(self, triangle: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def dp(i, j):
            # 递归 动态规划
            if i == len(triangle)-1:
                return triangle[i][j]
            return triangle[i][j] + min(dp(i+1, j), dp(i+1, j+1))
        return dp(0,0)
    def dp_grid(self, triangle: List[List[int]]) -> int:
        # 状态动态规划
        dp = triangle[-1]
        for i in range(len(triangle)-2,-1,-1):
            for j in range(i+1):
                dp[j] = triangle[i][j] + min(dp[j],dp[j+1])
        return dp[0]
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return {
            1:lambda triangle:self.recursion(triangle),
            2:lambda triangle:self.dp_grid(triangle)
        }[2](triangle)
        # n = len(triangle)
        # f = [0] * n
        # f[0] = triangle[0][0]

        # for i in range(1, n):
        #     print(f)
        #     f[i] = f[i - 1] + triangle[i][i]
        #     print(f)
        #     for j in range(i - 1, 0, -1):
        #         print(f)
        #         f[j] = min(f[j - 1], f[j]) + triangle[i][j]
        #         print(f)
        #     f[0] += triangle[i][0]
            
        # print(min(f))
        # return min(f)


# @lc code=end
if __name__ == "__main__":
    test = Solution()
    test.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
