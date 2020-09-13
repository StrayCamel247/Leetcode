#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#
# https://leetcode-cn.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (69.11%)
# Likes:    802
# Dislikes: 0
# Total Accepted:    84.6K
# Total Submissions: 122.5K
# Testcase Example:  '3'
#
# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
#
# 示例:
#
# 输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
#
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
#
#
from functools import lru_cache
# @lc code=start
class Solution(object):
    def Catalan(self, n) -> int:
        C = 1
        for _ in range(0, n):
            C *= 2*(2*_+1)/(_+2)
        return int(C)

    def dynamic_programing(self, n):
        """ G(n)G(n): 长度为 nn 的序列能构成的不同二叉搜索树的个数。
        """
        G = [0]*(n+1)
        G[0], G[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                print(G)
                G[i] += G[j-1] * G[i-j]

        return G[n]

    @lru_cache(None)
    def numTrees(self, n):
        # 递归法
        if n <= 0: return 1
        if n <= 2: return n
        return sum([self.numTrees(i-1) * self.numTrees(n-i) for i in range(1, n + 1)])


# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.numTrees(3))
