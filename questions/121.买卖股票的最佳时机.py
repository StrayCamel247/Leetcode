#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (53.82%)
# Likes:    891
# Dislikes: 0
# Total Accepted:    182.3K
# Total Submissions: 338.8K
# Testcase Example:  '[7,1,5,3,6,4]'
#
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
# 
# 注意：你不能在买入股票前卖出股票。
# 
# 
# 
# 示例 1:
# 
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
# ⁠    注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
# 
# 
# 示例 2:
# 
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
# 
# 
#

# @lc code=start
from typing import List
class Solution:
    """
    动态规划

    """
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:return 0
        # 只买卖一次
        dp = 0
        dp1 = -prices[0]
        dp2 = float('-inf')
        for _ in prices[1:]:
            dp1=max(dp1, dp-_)
            dp2=max(dp2, dp1+_)
        return max(dp2,dp)

# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.maxProfit(prices=[7,1,5,3,6,4]))
