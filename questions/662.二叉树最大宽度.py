#
# @lc app=leetcode.cn id=662 lang=python3
#
# [662] 二叉树最大宽度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.leftIds = []
        self.widths = []
    
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        return self.dfs(root, 0, 0)
    
    def dfs(self, node, depth, id):
        # node: current node of the current layer
        # depth: depth of a tree, starting from 0
        # id: current id of the node
        # returns the max width of all layers
        if node == None:
            return 0
        if len(self.leftIds) == depth:
            self.leftIds.append(id)
            self.widths.append(1)
        else:
            self.widths[depth] = id - self.leftIds[depth] + 1
            
        leftMaxWidth = self.dfs(node.left, depth + 1, id * 2)
        rightMaxWidth = self.dfs(node.right, depth + 1, id * 2 + 1)
            
        return max(max(leftMaxWidth, rightMaxWidth), self.widths[depth])
# @lc code=end
