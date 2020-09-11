#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#
# https://leetcode-cn.com/problems/edit-distance/description/
#
# algorithms
# Hard (59.28%)
# Likes:    773
# Dislikes: 0
# Total Accepted:    51.1K
# Total Submissions: 86.2K
# Testcase Example:  '"horse"\n"ros"'
#
# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
# 
# 你可以对一个单词进行如下三种操作：
# 
# 
# 插入一个字符
# 删除一个字符
# 替换一个字符
# 
# 
# 
# 
# 示例 1：
# 
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
# 
# 
# 示例 2：
# 
# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
# 
# 
#

# @lc code=start
class Solution:
    def grid_dp(self, word1: str, word2: str) -> int:
        # 经典的状态动态规划
        # grid[i][j] = min(grid[i][j-1]+1, grid[i-1][j]+1, grid[i-1][j-1])-1
        row,col = len(word1),len(word2)
        # 有一个字符串为空串
        if row * col == 0:return row + col
        # 初始化DP数组
        grid = [ [_]+[i if not _ else 0 for i in range(1,col+1) ] for _ in range(row + 1)]
        # [[0, 1, 2, 3], 
        # [1, 0, 0, 0], 
        # [2, 0, 0, 0], 
        # [3, 0, 0, 0],
        # [4, 0, 0, 0], 
        # [5, 0, 0, 0]]
        
        # 计算所有 DP 值
        for _row in range(1, row + 1):
            for _col in range(1, col + 1):
                left = grid[_row - 1][_col] + 1
                down = grid[_row][_col - 1] + 1
                left_down = grid[_row - 1][_col - 1] 
                # 如果word1和word2最后一个char相同
                left_down += word1[_row - 1] != word2[_col - 1]

                grid[_row][_col] = min(left, down, left_down)
        
        return grid[row][col]

    def minDistance(self, word1: str, word2: str) -> int:
        # Accepted
        #     1146/1146 cases passed (140 ms)
        #     Your runtime beats 93.22 % of python3 submissions
        #     Your memory usage beats 90.68 % of python3 submissions (16.5 MB)
        import functools
        @functools.lru_cache(None)
        def helper(i, j):
            if i == len(word1) or j == len(word2):
                return len(word1) - i + len(word2) - j
            if word1[i] == word2[j]:
                return helper(i + 1, j + 1)
            else:
                inserted = helper(i, j + 1)
                deleted = helper(i + 1, j)
                replaced = helper(i + 1, j + 1)
                return min(inserted, deleted, replaced) + 1
        return helper(0, 0)
# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.minDistance(word1 = "horse", word2 = "ros"))
