/*
 * @lc app=leetcode.cn id=188 lang=golang
 *
 * [188] 买卖股票的最佳时机 IV
 *
 * https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/description/
 *
 * algorithms
 * Hard (36.44%)
 * Likes:    477
 * Dislikes: 0
 * Total Accepted:    65.3K
 * Total Submissions: 177.1K
 * Testcase Example:  '2\n[2,4,1]'
 *
 * 给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
 *
 * 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
 *
 * 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：k = 2, prices = [2,4,1]
 * 输出：2
 * 解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
 *
 * 示例 2：
 *
 *
 * 输入：k = 2, prices = [3,2,6,5,0,3]
 * 输出：7
 * 解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
 * ⁠    随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 =
 * 3 。
 *
 *
 *
 * 提示：
 *
 *
 * 0
 * 0
 * 0
 *
 *
 */

// @lc code=start
func maxProfit(k int, prices []int) int {

	if len(prices) == 0 {
		return 0
	}
	n := len(prices)

	if k > n/2 {
		return bf(prices)
	}

	dp := make([][]int, k+1)
	for i := 0; i < k+1; i++ {
		dp[i] = make([]int, n+1)
	}

	// dp[k][i] = max(dp[k][i-1], prices[i] - prices[j] + dp[k-1][j-1])
	for j := 1; j < k+1; j++ {
		min_price := prices[0]
		for i := 1; i < n+1; i++ {
			min_price = Min(min_price, prices[i-1]-dp[j-1][i-1])
			dp[j][i] = Max(dp[j][i-1], prices[i-1]-min_price)
		}
	}

	return dp[k][n]
}

func bf(prices []int) int {
	profit := 0
	for i := 1; i < len(prices); i++ {
		if prices[i] > prices[i-1] {
			profit += (prices[i] - prices[i-1])
		}
	}
	return profit
}

func Min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

// @lc code=end

