#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#
# https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (54.10%)
# Likes:    173
# Dislikes: 0
# Total Accepted:    42K
# Total Submissions: 77.7K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
# 
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回锯齿形层次遍历如下：
# 
# [
# ⁠ [3],
# ⁠ [20,9],
# ⁠ [15,7]
# ]
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import List
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        def deeper(root, depth):
            if not root:return
            if len(res) == depth:
                res.append([])
            print(depth, res)
            #  depth % 2 决定插入数据的顺序，如果是偶数，证明是从左至右，如果是奇数，从右至左
            if depth % 2 == 0:res[depth].append(root.val)
            else: res[depth].insert(0, root.val)
            deeper(root.left, depth + 1)
            deeper(root.right, depth + 1)
        deeper(root, 0)
        return res

# @lc code=end
if __name__ == "__main__":
    print(Solution.zigzagLevelOrder([3,9,20,0,0,15,7]))
