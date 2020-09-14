#
# @lc app=leetcode.cn id=498 lang=python3
#
# [498] 对角线遍历
#
# https://leetcode-cn.com/problems/diagonal-traverse/description/
#
# algorithms
# Medium (42.04%)
# Likes:    124
# Dislikes: 0
# Total Accepted:    23.8K
# Total Submissions: 56.5K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。
#
#
#
# 示例:
#
# 输入:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
#
# 输出:  [1,2,4,7,5,3,6,8,9]
#
# 解释:
#
#
#
#
#
# 说明:
#
#
# 给定矩阵中的元素总数不会超过 100000 。
#
#
#
from typing import List
import collections
# @lc code=start
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        lookup = collections.defaultdict(list)
        
        row, col = len(matrix), len(matrix[0])

        for i in range(row):
            for j in range(col):
                lookup[j + i].append(matrix[i][j])
        
        res = []
        flag = True
        for k, v in sorted(lookup.items()):
            if flag:
                res.extend(v[::-1])
            else:
                res.extend(v)
            flag = not flag
        return res

# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))