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
    def recursion(self, N, K):
        def _help(n):
            if n == 1:
                return '0'
            return _help(n-1)+''.join(['1' if _ == '0' else '0' for _ in _help(n-1)])
        return _help(N)[K-1]

    def nonequivalence(self, N, K):
        if N == 1:
            return 0
        return (1 - K % 2) ^ self.kthGrammar(N-1, (K+1)//2)
    def fold_recursion(self, N, K):
        if N == 1: return 0
        if K <= (1 << N-2):
            return self.kthGrammar(N-1, K)
        return self.kthGrammar(N-1, K - (1 << N-2)) ^ 1
    def bite_operation(self, N, K):
        print(bin(K - 1))
        return bin(K - 1).count('1') % 2
    def kthGrammar(self, N, K):
        return {
            1: lambda N, K: self.recursion(N, K),
            2: lambda N, K: self.nonequivalence(N, K),
            3: lambda N, K: self.fold_recursion(N, K),
            4: lambda N, K: self.bite_operation(N, K),
        }[4](N, K)
        return bin(K -1).count('1') % 2


# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.kthGrammar(8,7))
    # string = """|  {a}  | {b}  |\n""".format(a=a,b=b)
    # for _ in range(1, 6):
    #     print("""|  {a}  | {b}  |\n""".format(a=_,b=test.kthGrammar(_,2)))
