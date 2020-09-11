#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#
# https://leetcode-cn.com/problems/linked-list-cycle-ii/description/
#
# algorithms
# Medium (49.64%)
# Likes:    432
# Dislikes: 0
# Total Accepted:    66.4K
# Total Submissions: 133.5K
# Testcase Example:  '[3,2,0,-4]\n1'
#
# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
# 
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
# 
# 说明：不允许修改给定的链表。
# 
# 
# 
# 示例 1：
# 
# 输入：head = [3,2,0,-4], pos = 1
# 输出：tail connects to node index 1
# 解释：链表中有一个环，其尾部连接到第二个节点。
# 
# 
# 
# 
# 示例 2：
# 
# 输入：head = [1,2], pos = 0
# 输出：tail connects to node index 0
# 解释：链表中有一个环，其尾部连接到第一个节点。
# 
# 
# 
# 
# 示例 3：
# 
# 输入：head = [1], pos = -1
# 输出：no cycle
# 解释：链表中没有环。
# 
# 
# 
# 
# 
# 
# 进阶：
# 你是否可以不用额外空间解决此题？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 链表查找，fast_slow快慢指针法
    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        # fast每次走两步，slow每次走一步
        while True:
            # fast走到头了，如果不是环形的，fast肯定比slow先走到头，只需要判断fast就好了
            if not (fast and fast.next): return 
            fast, slow = fast.next.next, slow.next
            # 如果是环形，肯定会碰到，break
            if fast == slow: break
        # 当是环形的，找到环形的index
        fast = head
        while fast!=slow:
            fast, slow = fast.next, slow.next
        return fast
        
# @lc code=end

