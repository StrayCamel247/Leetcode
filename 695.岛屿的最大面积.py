#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#
# https://leetcode-cn.com/problems/max-area-of-island/description/
#
# algorithms
# Medium (63.21%)
# Likes:    251
# Dislikes: 0
# Total Accepted:    40.4K
# Total Submissions: 63.9K
# Testcase Example:  '[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]'
#
# 给定一个包含了一些 0 和 1 的非空二维数组 grid 。
# 
# 一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被
# 0（代表水）包围着。
# 
# 找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)
# 
# 
# 
# 示例 1:
# 
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,1,1,0,1,0,0,0,0,0,0,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,0,1,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,1,1,0,0],
# ⁠[0,0,0,0,0,0,0,0,0,0,1,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 
# 
# 对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。
# 
# 示例 2:
# 
# [[0,0,0,0,0,0,0,0]]
# 
# 对于上面这个给定的矩阵, 返回 0。
# 
# 
# 
# 注意: 给定的矩阵grid 的长度和宽度都不超过 50。
# 
#

# @lc code=start
"""深度优先搜索"""
from typing import List
class Solution:
    def dfs(self, grid, i, j):
        if  0<=i<self.rows and  0<=j<self.columns and grid[i][j]:
            # 当当前位置[i][j]为1时，覆盖为0，并判断上下左右的地区是否为1（因为在进行递归判断的时候，可能会导致先前位置判断重复，所以需要覆盖为0）
            grid[i][j] = 0
            return 1 + self.dfs(grid, i+1,j) + self.dfs(grid, i-1, j) + self.dfs(grid, i, j+1) + self.dfs(grid, i, j-1)
        return 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 获取grid的行和列
        self.rows, self.columns = len(grid), len(grid[0])
        result = 0
        for x in range(self.rows):
            for y in range(self.columns):
                result = max(result, self.dfs(grid, x, y))
        return result

        
# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))
