#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
'''
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

'''

class Solution(object):
    def test(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]
    
    def test1(self, 
        text : "被匹配数", 
        pattern:"匹配因子"):
        '''
        递归函数对每pattern[0]和text[0进行判断
        '''

        # 当匹配因子pattern为none，若被匹配数text也为none则为ture，否则无论被匹配数text为任何值，都返回false。
        if not pattern:
            return not text
        
        # 第一次匹配布尔值first_match
        # 若first_match为真，则只可能是 text 不为空且 （`pattern[0] == '.'` 或者`pattern[0] == text[0]`）
        first_match = bool(text) and pattern[0] in {text[0], '.'}


        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        # 如果pattern长度只为1，则只需判断first_match是否为空且继续对text[1:], pattern[1:]进行递归判断
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])
        
    def isMatch(self, text, pattern):
        return {
            1 : lambda text, pattern:self.test1(text, pattern),
        }[1](text, pattern)
        
# @lc code=end
if __name__ == "__main__":
    test = Solution()
    s = "mississippi"
    p = "mis*is*p*."
    print(test.isMatch(s,p))