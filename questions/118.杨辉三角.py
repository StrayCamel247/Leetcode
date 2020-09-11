#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
from typing import List
from math import factorial
# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        _ = lambda n, r: factorial(n) // factorial(r) // factorial(n - r)
        return [[_(n, r) for r in range(n + 1)] for n in range(numRows)]

        # iteration
        # if numRows == 0: return []
        # res = [[1]]
        # while len(res) < numRows:
        #     newRow = [a+b for a, b in zip([0]+res[-1], res[-1]+[0])]
        #     res.append(newRow)
        # return res
# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.generate(5))
    # [[1], 
    # [1, 1], 
    # [1, 2, 1], 
    # [1, 3, 3, 1], 
    # [1, 4, 6, 4, 1]]
    def _(n,r):
        print(n,r,':',factorial(n) , factorial(r) , factorial(n - r),factorial(n) // factorial(r) // factorial(n - r))
        return factorial(n) // factorial(r) // factorial(n - r)
    for n in range(5):
        for r in range(n+1):
            print(_(n, r))
