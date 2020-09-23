#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # s.reverse()
        # 双指针
        left , right = 0, len(s)-1
        while left<right:
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1
# @lc code=end

