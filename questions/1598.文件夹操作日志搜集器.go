/*
 * @lc app=leetcode.cn id=1598 lang=golang
 *
 * [1598] 文件夹操作日志搜集器
 */

// @lc code=start
func minOperations(logs []string) int {
	level := 0
	for i := 0; i < len(logs); i++ {
		if logs[i] == "../" {
			if level > 0 {
				level--
			}
		} else if logs[i] != "./" {
			level++
		}
	}
	return level
}

// @lc code=end

