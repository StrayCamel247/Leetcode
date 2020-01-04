#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
import dis
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # y = 
        return str(x)== str(x)[::-1] 
# @lc code=end
if __name__ == "__main__":
    from datetime import datetime

    def check1(x):
        y = str(x)[::-1]
        return str(x)== y

    def check2(x):
            return str(x)==str(x)[::-1]

    size = 10000000

    def call(func):
        start_time = datetime.now()
        for i in range(size):
            result = func(123456789)
        print(datetime.now() - start_time,':',func.__name__)
    
    call(check2)
    call(check1)