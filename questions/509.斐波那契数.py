#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, N: int) -> int:
        if N < 2:
            return N
        return self.fib(N-1)+self.fib(N-2)
        
# @lc code=end

