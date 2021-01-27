#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#
# https://leetcode-cn.com/problems/house-robber-iii/description/
#
# algorithms
# Medium (60.93%)
# Likes:    705
# Dislikes: 0
# Total Accepted:    82.3K
# Total Submissions: 134.9K
# Testcase Example:  '[3,2,3,null,3,null,1]'
#
# 在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。
# 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
# 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
#
# 计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
#
# 示例 1:
#
# 输入: [3,2,3,null,3,null,1]
#
# ⁠    3
# ⁠   / \
# ⁠  2   3
# ⁠   \   \
# ⁠    3   1
#
# 输出: 7
# 解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
#
# 示例 2:
#
# 输入: [3,4,5,1,3,null,1]
#
#     3
# ⁠   / \
# ⁠  4   5
# ⁠ / \   \
# ⁠1   3   1
#
# 输出: 9
# 解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# import functools
class Solution:

    def rob(self, root: TreeNode) -> int:
        # @functools.lru_cache(None)
        def _rob(root):
            if not root: return 0, 0
            
            rob_left, unrob_left = _rob(root.left)
            rob_right, unrob_right = _rob(root.right)
            
            return root.val + unrob_left + unrob_right, max(rob_left, unrob_left) + max(rob_right, unrob_right)

        return max(_rob(root))
    

# @lc code=end
