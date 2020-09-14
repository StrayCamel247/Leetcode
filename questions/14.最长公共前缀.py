#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (36.83%)
# Likes:    951
# Dislikes: 0
# Total Accepted:    223.2K
# Total Submissions: 605.7K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 示例 1:
# 
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 
# 
# 示例 2:
# 
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 
# 
# 说明:
# 
# 所有输入只包含小写字母 a-z 。
# 
#
from typing import List
# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:return ''
        _ = min(strs, key=len) 
        strs.remove(_)
        for s in strs:
            while s.find(_)!=0:
                _ = _[:-1]
        return _
        
        # 找公共字符串可以用zip法if not strs:return ''
        # res = ''
        # for x in zip(*strs):
        #     if len(set(x)) == 1:
        #         res+=x[0]
        #     else:
        #         break
        # return res
        
# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.longestCommonPrefix(["ca","a"]))

