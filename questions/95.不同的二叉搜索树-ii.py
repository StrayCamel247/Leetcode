#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#
# https://leetcode-cn.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (66.68%)
# Likes:    629
# Dislikes: 0
# Total Accepted:    60.6K
# Total Submissions: 90.9K
# Testcase Example:  '3'
#
# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。
# 
# 
# 
# 示例：
# 
# 输入：3
# 输出：
# [
# [1,null,3,2],
# [3,2,null,1],
# [3,1,null,null,2],
# [2,1,3],
# [1,null,2,null,3]
# ]
# 解释：
# 以上的输出对应以下 5 种不同结构的二叉搜索树：
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= n <= 8
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def _generateTrees(start, end):
            if start>end:
                return [None, ]
            all_trees = []
            for _ in range(start, end+1):
                left_trees = _generateTrees(start, _-1)
                right_trees = _generateTrees(_+1, end)
                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(_)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)
            return all_trees
        return _generateTrees(1, n) if n else []
# @lc code=end

