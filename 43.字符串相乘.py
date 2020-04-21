#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#
# https://leetcode-cn.com/problems/multiply-strings/description/
#
# algorithms
# Medium (42.01%)
# Likes:    308
# Dislikes: 0
# Total Accepted:    54.6K
# Total Submissions: 129.9K
# Testcase Example:  '"2"\n"3"'
#
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
# 
# 示例 1:
# 
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
# 
# 示例 2:
# 
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
# 
# 说明：
# 
# 
# num1 和 num2 的长度小于110。
# num1 和 num2 只包含数字 0-9。
# num1 和 num2 均不以零开头，除非是数字 0 本身。
# 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
# 
# 
#

# @lc code=start
class Solution:
    def vertical_multiplication(self, num1: str, num2: str) -> str:
        """竖式乘法"""
        a = num1[::-1]
        b = num2[::-1]
        result = 0
        
        for i,x in enumerate(a):
            temp_result = 0
            for j,y in enumerate(b):
                temp_result += int(x) * int(y) * 10**j
            result += temp_result * 10**i
        return str(result)

    def multiply(self, num1: str, num2: str) -> str:
        return {
            # eval() 函数用来执行一个字符串表达式，并返回表达式的值。
            1 : lambda num1, num2: (str(eval(num1+'*'+num2))),
            2 : lambda num1, num2: self.vertical_multiplication(num1, num2),
        }[2]( num1, num2)

# @lc code=end
if __name__ == "__main__":
    test = Solution()
    test.multiply(num1 = "2", num2 = "3")

