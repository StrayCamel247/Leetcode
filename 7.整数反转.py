#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse_force(self, x: int) -> int:
        if -10 < x < 10:
            return x

        str_x = str(x)
        if str_x[0] != "-":
            str_x = str_x[::-1]
            x = int(str_x)
        else:
            str_x = str_x[:0:-1]
            x = int(str_x)
            x = -x

        return x if -2147483648 < x < 2147483647 else 0

    def reverse_better(
        self, 
        x: int) -> int:
        '''
        复习一下python的位运算符：
        a = 0011 1100
        b = 0000 1101
        时间复杂度：O(log(x))，x中大约有log10(x) 位数字。
        空间复杂度：O(1)
        - a << 2 	
        左移动运算符：运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0。
        输出结果 240 ，二进制解释： 1111 0000

        - a >> 2 
        右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，>> 右边的数字指定了移动的位数	
        输出结果 15 ，二进制解释： 0000 1111
        '''
        
        y, res = abs(x), 0
        # 则其数值范围为 [−2^31,  2^31 − 1]
        boundry = (1<<31) -1 if x>0 else 1<<31
        while y != 0:
            res = res*10 +y%10
            if res > boundry :
                return 0
            y //=10
        return res if x >0 else -res

    def reverse(self, x: int) -> int:
        return {
            1 : lambda x:self.reverse_force(x),
            2 : lambda x:self.reverse_better(x),
        }[1](x)

        
# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.reverse_force(-123))
