/*
 * @lc app=leetcode.cn id=102 lang=golang
 *
 * [102] 二叉树的层序遍历
 *
 * https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/
 *
 * algorithms
 * Medium (64.18%)
 * Likes:    806
 * Dislikes: 0
 * Total Accepted:    267.2K
 * Total Submissions: 416.2K
 * Testcase Example:  '[3,9,20,null,null,15,7]'
 *
 * 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
 *
 *
 *
 * 示例：
 * 二叉树：[3,9,20,null,null,15,7],
 *
 *
 * ⁠   3
 * ⁠  / \
 * ⁠ 9  20
 * ⁠   /  \
 * ⁠  15   7
 *
 *
 * 返回其层序遍历结果：
 *
 *
 * [
 * ⁠ [3],
 * ⁠ [9,20],
 * ⁠ [15,7]
 * ]
 *
 *
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func levelOrder(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}
	var res [][]int
	queue := []*TreeNode{root}
	for level := 0; len(queue) > 0; level++ { //level - to track where we need to insert values
		res = append(res, []int{}) //adding slice for the new "level" of values
		for levelSize := len(queue); levelSize > 0; levelSize-- {
			//levelSize - to track how many elements we need to dequeue and insert in the current "level"
			if queue[0].Left != nil {
				queue = append(queue, queue[0].Left)
			} //adding next nodes to the queue
			if queue[0].Right != nil {
				queue = append(queue, queue[0].Right)
			}
			res[level] = append(res[level], queue[0].Val) //adding first element in the queue to a "level" slice
			queue = queue[1:]                             //deque first element
		}
	}
	return res
}

// @lc code=end

