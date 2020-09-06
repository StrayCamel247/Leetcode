#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
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
        self.res = []
    
    def dfs(self, root: TreeNode):
        if not root:return []
        return self.dfs(root.left)+[root.val]+self.dfs(root.right)
    
    def iterative(self, root: TreeNode):
        if not root:return []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            self.res.append(cur.val)
            cur = cur.right
        return self.res
            
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归法 dfs
        # return self.dfs(root)
        # 迭代法
        return self.dfs(root)
# @lc code=end

