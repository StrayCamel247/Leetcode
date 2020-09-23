#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
# https://leetcode-cn.com/problems/search-insert-position/description/
#
# algorithms
# Easy (46.67%)
# Likes:    682
# Dislikes: 0
# Total Accepted:    246.3K
# Total Submissions: 527.6K
# Testcase Example:  '[1,3,5,6]\n5'
#
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 
# 你可以假设数组中无重复元素。
# 
# 示例 1:
# 
# 输入: [1,3,5,6], 5
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: [1,3,5,6], 2
# 输出: 1
# 
# 
# 示例 3:
# 
# 输入: [1,3,5,6], 7
# 输出: 4
# 
# 
# 示例 4:
# 
# 输入: [1,3,5,6], 0
# 输出: 0
# 
# 
#
from typing import List
from bisect import bisect_left
# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # bisection
        x = 0
        y = len(nums)
        while x < y:
            mid = (x+y)//2
            if nums[mid] < target: x = mid+1
            else: y = mid
        return x
        # return bisect_left(nums, target)
# @lc code=end
if __name__ == "__main__":
    test=Solution()
    print(test.searchInsert([1,2,3], 7))
