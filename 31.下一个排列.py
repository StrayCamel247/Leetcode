#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
# https://leetcode-cn.com/problems/next-permutation/description/
#
# algorithms
# Medium (34.45%)
# Likes:    636
# Dislikes: 0
# Total Accepted:    85.9K
# Total Submissions: 249.3K
# Testcase Example:  '[1,2,3]'
#
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
# 
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
# 
# 必须原地修改，只允许使用额外常数空间。
# 
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 
#
from typing import *
# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1: return

        p = len(nums) - 2
        while p >= 0:
            if nums[p] >= nums[p+1]:
                p -= 1
                continue
    
            for idx in range(p+1,len(nums)):
                if nums[idx] <= nums[p]:
                    idx -= 1
                    break
            nums[p],nums[idx]=nums[idx],nums[p]
            lst = sorted(nums[p+1:])     

            for i in range(len(lst)):
                nums[i+p+1] = lst[i]
            return 

        nums.reverse() 

            

# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.nextPermutation([1,1,5]))