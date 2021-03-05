/*
 * @lc app=leetcode.cn id=1573 lang=golang
 *
 * [1573] 分割字符串的方案数
 *
 * https://leetcode-cn.com/problems/number-of-ways-to-split-a-string/description/
 *
 * algorithms
 * Medium (28.76%)
 * Likes:    3
 * Dislikes: 0
 * Total Accepted:    3.5K
 * Total Submissions: 12.1K
 * Testcase Example:  '"10101"'
 *
 * 给你一个二进制串 s  （一个只包含 0 和 1 的字符串），我们可以将 s 分割成 3 个 非空 字符串 s1, s2, s3 （s1 + s2 +
 * s3 = s）。
 *
 * 请你返回分割 s 的方案数，满足 s1，s2 和 s3 中字符 '1' 的数目相同。
 *
 * 由于答案可能很大，请将它对 10^9 + 7 取余后返回。
 *
 *
 *
 * 示例 1：
 *
 * 输入：s = "10101"
 * 输出：4
 * 解释：总共有 4 种方法将 s 分割成含有 '1' 数目相同的三个子字符串。
 * "1|010|1"
 * "1|01|01"
 * "10|10|1"
 * "10|1|01"
 *
 *
 * 示例 2：
 *
 * 输入：s = "1001"
 * 输出：0
 *
 *
 * 示例 3：
 *
 * 输入：s = "0000"
 * 输出：3
 * 解释：总共有 3 种分割 s 的方法。
 * "0|0|00"
 * "0|00|0"
 * "00|0|0"
 *
 *
 * 示例 4：
 *
 * 输入：s = "100100010100110"
 * 输出：12
 *
 *
 *
 *
 * 提示：
 *
 *
 * s[i] == '0' 或者 s[i] == '1'
 * 3 <= s.length <= 10^5
 *
 *
 */

// @lc code=start
func numWays(s string) int {
	sLen := len(s)
	n := strings.Count(s, "1")
	mod := 1000000007
	ans := 0
	if n == 0 {
		ans = ((sLen - 1) * (sLen - 2) / 2) % mod
	} else if n%3 == 0 {
		m := n / 3
		m1 := 1
		m2 := 1
		k := 0
		for i := 0; i < len(s); i++ {
			if s[i] == '1' {
				k++
				if k > 2*m {
					break
				}
			} else {
				if k == m {
					m1++
				} else if k == 2*m {
					m2++
				}
			}
		}
		ans = m1 * m2 % mod
	}
	return ans
}

// @lc code=end

