#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
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
        if len(nums)<3 :return max(*(nums+[0,0]))
        grid= [0] * len(nums)
        grid[0] = nums[0]
        grid[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            grid[i] = max(grid[i - 1], grid[i - 2] + nums[i])
        return max(grid)

        
        
# @lc code=end
if __name__ == "__main__":
    test = Solution()
