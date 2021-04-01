#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/description/
#
# algorithms
# Hard (36.44%)
# Likes:    477
# Dislikes: 0
# Total Accepted:    65.3K
# Total Submissions: 177.1K
# Testcase Example:  '2\n[2,4,1]'
#
# 给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
# 
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
# 
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：k = 2, prices = [2,4,1]
# 输出：2
# 解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
# 
# 示例 2：
# 
# 
# 输入：k = 2, prices = [3,2,6,5,0,3]
# 输出：7
# 解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
# ⁠    随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3
# 。
# 
# 
# 
# 提示：
# 
# 
# 0 
# 0 
# 0 
# 
# 
#

# @lc code=start
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        n = len(prices)
        k = min(k, n // 2)
        buy = [- prices[0]] + [float('-inf')]*k
        sell = [0] + [float('-inf')]*k
        # 遍历
        for i in range(1, n):
            buy[0] = max(buy[0], sell[0] - prices[i])
            for j in range(1, 1 + k):
                buy[j] = max(buy[j], sell[j] - prices[i])
                # 当天持有股票的收益，等于昨日就持有股票 和 昨日为持有股票并买入股票之间的较大值
                sell[j] = max(sell[j], buy[j - 1] + prices[i]) 

        return max(sell)

# @lc code=end

