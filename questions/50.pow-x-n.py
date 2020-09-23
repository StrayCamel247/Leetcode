#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 二分法 log(n)
        def _help(N):
            if N == 0:
                return 1.0
            y = _help(N // 2)
            return y * y if N % 2 == 0 else y * y * x
        
        return _help(n) if n >= 0 else 1.0 / _help(-n)

# @lc code=end

