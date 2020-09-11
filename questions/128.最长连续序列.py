#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
# https://leetcode-cn.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (48.43%)
# Likes:    288
# Dislikes: 0
# Total Accepted:    33.9K
# Total Submissions: 70K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# 给定一个未排序的整数数组，找出最长连续序列的长度。
# 
# 要求算法的时间复杂度为 O(n)。
# 
# 示例:
# 
# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
# 
#

# @lc code=start
from typing import List
class Solution:
    def longestConsecutive(self, nums):
        """
        时间复杂度：O(nlgn)O(nlgn)

        算法核心的 for循环恰好运行 nn 次，所以算法的时间复杂度由 sort 函数的调用决定，通常会采用 O(nlgn)O(nlgn) 时间复杂度的算法。
        """
        if not nums:return 0
        nums.sort()
        res = 1
        tmp = 1
        print(nums)
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    tmp += 1
                else:
                    res = max(res, tmp)
                    tmp = 1

        return max(res, tmp)


        
# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.longestConsecutive([100,4,200,1,3,2]))
