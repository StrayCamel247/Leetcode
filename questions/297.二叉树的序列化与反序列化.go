/*
 * @lc app=leetcode.cn id=297 lang=golang
 *
 * [297] 二叉树的序列化与反序列化
 *
 * https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/description/
 *
 * algorithms
 * Hard (53.93%)
 * Likes:    528
 * Dislikes: 0
 * Total Accepted:    74.2K
 * Total Submissions: 136.8K
 * Testcase Example:  '[1,2,3,null,null,4,5]'
 *
 *
 * 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
 *
 * 请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 /
 * 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
 *
 * 提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode
 * 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：root = [1,2,3,null,null,4,5]
 * 输出：[1,2,3,null,null,4,5]
 *
 *
 * 示例 2：
 *
 *
 * 输入：root = []
 * 输出：[]
 *
 *
 * 示例 3：
 *
 *
 * 输入：root = [1]
 * 输出：[1]
 *
 *
 * 示例 4：
 *
 *
 * 输入：root = [1,2]
 * 输出：[1,2]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 树中结点数在范围 [0, 10^4] 内
 * -1000
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

// BFS solution

import (
	"strconv"
	"strings"
)

const (
	Empty     = "E"
	Delimiter = ","
)

type Codec struct {
}

func Constructor() Codec {
	return Codec{}
}

// Serializes a tree to a single string.
func (this *Codec) serialize(root *TreeNode) string {
	if root == nil {
		return ""
	}

	queue := []*TreeNode{root}
	tree := []string{}

	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]

		if node == nil {
			tree = append(tree, Empty)
			continue
		}

		tree = append(tree, fmt.Sprintf("%d", node.Val))

		queue = append(queue, node.Left)
		queue = append(queue, node.Right)
	}

	return strings.Join(tree, Delimiter)
}

// Deserializes your encoded data to tree.
func (this *Codec) deserialize(data string) *TreeNode {
	if len(data) == 0 {
		return nil
	}

	tokens := strings.Split(data, Delimiter)
	queue := []*TreeNode{}

	d, _ := strconv.Atoi(tokens[0])
	root := &TreeNode{Val: d}
	queue = append(queue, root)
	index := 1

	for len(queue) > 0 && index < len(tokens) {
		node := queue[0]
		queue = queue[1:]

		node.Left = this.makeNode(tokens[index])
		index++
		node.Right = this.makeNode(tokens[index])
		index++

		if node.Left != nil {
			queue = append(queue, node.Left)
		}
		if node.Right != nil {
			queue = append(queue, node.Right)
		}
	}

	return root
}

func (this *Codec) makeNode(s string) *TreeNode {
	if s == Empty {
		return nil
	}

	d, _ := strconv.Atoi(s)
	return &TreeNode{Val: d}
}

/**
 * Your Codec object will be instantiated and called as such:
 * ser := Constructor();
 * deser := Constructor();
 * data := ser.serialize(root);
 * ans := deser.deserialize(data);
 */
// @lc code=end

