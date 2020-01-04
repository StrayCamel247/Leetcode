#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start


import re
class Solution:
    def myAtoi(self, str: str) -> int:
        '''
        使用正则表达式 ^：匹配字符串开头，
        [\+\-]：代表一个+字符或-字符，
        ?：前面一个字符可有可无，
        \d：一个数字，
        +：前面一个字符的一个或多个，
        \D：一个非数字字符，
        *：前面一个字符的0个或多个
        max(min(数字, 2**31 - 1), -2**31)
        '''
        
        return max(min(int(*re.findall('^[\+\-]?\d+', str.strip( ))), 2**31 - 1), -2**31)

# @lc code=end

if __name__ == "__main__":
    test = Solution()
    print(test.myAtoi("4193 with word"))