#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
# https://leetcode-cn.com/problems/house-robber/description/
#
# algorithms
# Easy (46.63%)
# Likes:    1056
# Dislikes: 0
# Total Accepted:    182.4K
# Total Submissions: 391K
# Testcase Example:  '[1,2,3,1]'
#
# 
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
# 
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
# 
# 
# 
# 示例 1：
# 
# 输入：[1,2,3,1]
# 输出：4
# 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
# 偷窃到的最高金额 = 1 + 3 = 4 。
# 
# 示例 2：
# 
# 输入：[2,7,9,3,1]
# 输出：12
# 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
# 偷窃到的最高金额 = 2 + 9 + 1 = 12 。
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= nums.length <= 100
# 0 <= nums[i] <= 400
# 
# 
#
from typing import List
import functools
# @lc code=start
class Solution:
    def dfs_recursion(self, nums: List[int]) -> int:
        @functools.lru_cache(None)
        def test(k=0):
            if len(nums[k:])==2:return max(nums[k:])
            if len(nums[k:])==3:return max(nums[k:][1], nums[k:][0]+nums[k:][2])
            return max(test(k+1), nums[k]+test(k+2))
        return test()
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3 :return max(nums+[0,0])
        grid= [0] * len(nums)
        grid[0] = nums[0]
        grid[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            grid[i] = max(grid[i - 1], grid[i - 2] + nums[i])
        return max(grid)

        
        
# @lc code=end
if __name__ == "__main__":
    test = Solution()


