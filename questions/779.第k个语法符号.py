#
# @lc app=leetcode.cn id=779 lang=python3
#
# [779] 第K个语法符号
#
# https://leetcode-cn.com/problems/k-th-symbol-in-grammar/description/
#
# algorithms
# Medium (42.72%)
# Likes:    90
# Dislikes: 0
# Total Accepted:    12.7K
# Total Submissions: 29.6K
# Testcase Example:  '1\n1'
#
# 在第一行我们写上一个 0。接下来的每一行，将前一行中的0替换为01，1替换为10。
# 
# 给定行数 N 和序数 K，返回第 N 行中第 K个字符。（K从1开始）
# 
# 
# 例子:
# 
# 输入: N = 1, K = 1
# 输出: 0
# 
# 输入: N = 2, K = 1
# 输出: 0
# 
# 输入: N = 2, K = 2
# 输出: 1
# 
# 输入: N = 4, K = 5
# 输出: 1
# 
# 解释:
# 第一行: 0
# 第二行: 01
# 第三行: 0110
# 第四行: 01101001
# 
# 
# 
# 注意：
# 
# 
# N 的范围 [1, 30].
# K 的范围 [1, 2^(N-1)].
# 
# 
#

# @lc code=start
class Solution(object):
    def kthGrammar(self, N, K):
        return bin(K -1).count('1') % 2
        
# @lc code=end

