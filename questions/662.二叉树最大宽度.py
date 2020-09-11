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
    def maxDepth(self, root: TreeNode) -> int:
        if not root:return 0
        # if root.left:
        #     return 1+self.maxDepth(root.left)
        # if root.right:
        #     return 1+maxDepth(root.right)
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
# @lc code=end

