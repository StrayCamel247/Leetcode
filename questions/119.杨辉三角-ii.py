#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#
from math import factorial
# @lc code=start
class Solution:
    def getRow(self, numRows: int) -> List[List[int]]:
        _ = lambda n, r: factorial(n) // factorial(r) // factorial(n - r)
        return [_(numRows, r) for r in range(numRows + 1)]
# @lc code=end

