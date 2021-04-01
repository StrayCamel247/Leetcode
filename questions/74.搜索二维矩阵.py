#
# @lc app=leetcode.cn id=74 lang=python
#
# [74] 搜索二维矩阵
#
# https://leetcode-cn.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (40.63%)
# Likes:    364
# Dislikes: 0
# Total Accepted:    98.4K
# Total Submissions: 232.7K
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3'
#
# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
# 
# 
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 
# -10^4 
# 
# 
#

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        二分查找
        """
        target_row = bisect.bisect_right([row[0] for row in matrix], target) - 1
        if target_row < 0:
            return False
        target_col = bisect.bisect_left(matrix[target_row], target)
        if target_col >= len(matrix[0]):
            return False
        if matrix[target_row][target_col] == target:
            return True
        return False

# @lc code=end

