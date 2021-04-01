/*
 * @lc app=leetcode.cn id=51 lang=golang
 *
 * [51] N 皇后
 *
 * https://leetcode-cn.com/problems/n-queens/description/
 *
 * algorithms
 * Hard (73.77%)
 * Likes:    811
 * Dislikes: 0
 * Total Accepted:    113.4K
 * Total Submissions: 153.6K
 * Testcase Example:  '4'
 *
 * n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
 *
 * 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
 *
 *
 *
 * 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：n = 4
 * 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
 * 解释：如上图所示，4 皇后问题存在两个不同的解法。
 *
 *
 * 示例 2：
 *
 *
 * 输入：n = 1
 * 输出：[["Q"]]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1
 * 皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。
 *
 *
 *
 *
 */

// @lc code=start
func solveNQueens(n int) [][]string {
	var col uint16
	ans := make([][]string, 0)
	// offset, x - y ranges from -n ~ n, convert it to 0 ~ 2n
	primary, secondary := make([]bool, 2*n), make([]bool, 2*n)

	backtracking(n, 0, []string{}, col, primary, secondary, &ans)

	return ans
}

func backtracking(n, row int, cur []string, col uint16, primary, secondary []bool, ans *[][]string) {
	if len(cur) == n {
		*ans = append(*ans, cur)
		return
	}

	for i := 0; i < n; i++ {
		// already used column, becareful, i == 0 means left most position
		offset := n - 1 - i
		if col&(1<<offset) > 0 {
			continue
		}

		// check diagonal
		// primary (\): x - y = constant
		// secondary (/): x + y = constant
		if primary[i-row+n] || secondary[i+row] {
			continue
		}

		primary[i-row+n] = true
		secondary[i+row] = true
		col |= 1 << offset

		str := make([]byte, n)
		for j := range str {
			str[j] = byte('.')
		}
		str[i] = byte('Q')

		tmp := make([]string, len(cur)+1)
		copy(tmp, cur)
		tmp[len(cur)] = string(str)

		backtracking(n, row+1, tmp, col, primary, secondary, ans)

		col = col ^ (1 << offset)
		primary[i-row+n] = false
		secondary[i+row] = false
	}
}

// @lc code=end

