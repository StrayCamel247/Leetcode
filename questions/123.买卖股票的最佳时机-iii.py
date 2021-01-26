#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/description/
#
# algorithms
# Hard (42.28%)
# Likes:    344
# Dislikes: 0
# Total Accepted:    30.3K
# Total Submissions: 71.6K
# Testcase Example:  '[3,3,5,0,0,3,1,4]'
#
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
#
# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
# 示例 1:
#
# 输入: [3,3,5,0,0,3,1,4]
# 输出: 6
# 解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
# 随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
#
# 示例 2:
#
# 输入: [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4
# 。
# 注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
# 因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
#
#
# 示例 3:
#
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。
#
#
from typing import List
# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 动态规划
        if not prices:
            return 0
        # 一直不买
        dp0 = 0
        # 只买一个
        dp1 = -prices[0]
        # 买一卖一
        dp2 = -float('inf')
        # 买二卖一
        dp3 = -float('inf')
        # 买二卖二
        dp4 = -float('inf')

        for _ in prices[0:]:
            dp1 = max(dp1, -_)
            dp2 = max(dp2, dp1+_)
            dp3 = max(dp3, dp2-_)
            dp4 = max(dp4, dp3+_)

        return max(dp0, dp2, dp4)


# @lc code=end
if __name__ == '__main__':

    test = Solution()
    print(test.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
