/*
 * @lc app=leetcode.cn id=117 lang=golang
 *
 * [117] 填充每个节点的下一个右侧节点指针 II
 *
 * https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/description/
 *
 * algorithms
 * Medium (59.51%)
 * Likes:    385
 * Dislikes: 0
 * Total Accepted:    66.6K
 * Total Submissions: 111.7K
 * Testcase Example:  '[1,2,3,4,5,null,7]'
 *
 * 给定一个二叉树
 *
 *
 * struct Node {
 * ⁠ int val;
 * ⁠ Node *left;
 * ⁠ Node *right;
 * ⁠ Node *next;
 * }
 *
 * 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
 *
 * 初始状态下，所有 next 指针都被设置为 NULL。
 *
 *
 *
 * 进阶：
 *
 *
 * 你只能使用常量级额外空间。
 * 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
 *
 *
 *
 *
 * 示例：
 *
 *
 *
 *
 * 输入：root = [1,2,3,4,5,null,7]
 * 输出：[1,#,2,3,#,4,5,7,#]
 * 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化输出按层序遍历顺序（由 next
 * 指针连接），'#' 表示每层的末尾。
 *
 *
 *
 * 提示：
 *
 *
 * 树中的节点数小于 6000
 * -100
 *
 *
 *
 *
 *
 *
 *
 */

// @lc code=start
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Left *Node
 *     Right *Node
 *     Next *Node
 * }
 */
func connect(root *Node) *Node {
	// 和层序遍历很像
	if root == nil {
		return nil
	}
	queue := make([]*Node, 0) //BFS queue
	queue = append(queue, root)

	for len(queue) > 0 {
		l := len(queue)
		for i := 0; i < l; i++ { //iterate the length of queue only
			node := queue[0]
			queue = queue[1:]
			if i < l-1 {
				node.Next = queue[0] //not the last node in this layer
			} else if i == l-1 {
				node.Next = nil //the last node in this layer
			}

			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
	}
	return root
}

// @lc code=end

