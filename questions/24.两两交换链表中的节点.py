#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # recursion
        if not head or not head.next:
            return head
        res = head.next
        head.next = self.swapPairs(res.next)
        res.next = head
        return res

        # iteration
        # res = None
        # while head and head.next:
        #     _res = head.next
        #     _res.next = head
        #     head = head.next.next
        #     if res:
        #         res.next = _res
        #     else:
        #         res = _res
        # return res
# @lc code=end

