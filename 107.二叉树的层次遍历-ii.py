#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import functools
from typing import List
class Solution:
    def __init__(self):
        self.res = {}

#     3
#    / \
#   9  20
#     /  \
#    15   7

    def iterative(self, root: TreeNode):
        # 迭代
        # Accepted
        #     34/34 cases passed (44 ms)
        #     Your runtime beats 64.23 % of python3 submissions
        #     Your memory usage beats 31.21 % of python3 submissions (14.1 MB)
        if not root:return []
        stack,cur,dep = [],root,0
        while stack or cur:
            while cur:
                stack.append((cur, dep))
                dep += 1
                cur = cur.left
            cur,dep = stack.pop()
            self.res[dep] = self.res.get(dep, []) +[cur.val]
            dep += 1
            cur = cur.right
        return [self.res[_] for _ in sorted(self.res.keys(), reverse=True)]
    @functools.lru_cache(None)
    def dfs(self, root: TreeNode, dep:int=0):
        # 递归对二叉树进行dfs，牺牲了内存，机器得爆掉
        # Accepted
        #   34/34 cases passed (40 ms)
        #   Your runtime beats 84.37 % of python3 submissions
        #   Your memory usage beats 5.09 % of python3 submissions (14.7 MB)MB)
        if not root:return []
        self.res[dep] = self.res.get(dep, []) +[root.val]
        dep +=1
        return self.dfs(root.left, dep)+self.dfs(root.right, dep)+[root.val]

    def queue(self, root: TreeNode) -> List[List[int]]:
        import collections
        # 队列法 感觉和迭代法没啥区别，官方函数collections.deque()还是值得看看https://docs.python.org/3.6/library/collections.html#collections.deque
        # Accepted
        #     34/34 cases passed (32 ms)
        #     Your runtime beats 98.8 % of python3 submissions
        #     Your memory usage beats 21.9 % of python3 submissions (14.1 MB)
        # queue = collections.deque([root])
        # res = []
        # while queue:
        #     size = len(queue)
        #     stock = []
        #     for _ in range(size):
        #         cur = queue.popleft()
        #         if not cur:
        #             continue
        #         stock.append(cur.val)
        #         queue.extend([cur.left,cur.right])
        #     if stock:
        #         res.insert(0,stock)
        # return res

        queue = [root]
        res = []
        while queue:
            size = len(queue)
            stock = []
            # print(queue)
            # stock = [queue.pop(_).val for _ in range(size) if queue[_]]
            # print(queue)
            # queue.extend([queue.pop(_).left for _ in range(size) if queue[_]])
            for _ in range(size):
                cur = queue.pop(0)
                if not cur:
                    continue
                stock.append(cur.val)
                queue.extend([cur.left,cur.right])
            if stock:
                res.insert(0,stock)
        return res
        
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        return {
            1: lambda root:(self.dfs(root), [self.res[_] for _ in reversed(self.res.keys())])[1],
            2: lambda root:self.iterative(root),
            3: lambda root:self.queue(root)
        }[1](root)
# @lc code=end
# if __name__ == "__main__":
#     test = Solution()
#     test.dfs
