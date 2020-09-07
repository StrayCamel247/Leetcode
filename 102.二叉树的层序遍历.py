#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res  = []
        
    def dfs(self, root):
        if not root:return []
    
    # 暴力法
    def brute(self, root):
        # Time Limit Exceeded
        stack = [root]
        while stack and root:
            tmp = []
            _res = []
            for _ in stack:
                _res.append(_.val)
                print(_)
                if _.left:tmp.append(_.left)
                if _.right:tmp.append(_.right)
            stack = tmp
            self.res.append(_res)
        return self.res
            
        
        
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        return self.brute(root)
# @lc code=end

