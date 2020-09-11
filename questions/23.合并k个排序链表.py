#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (49.73%)
# Likes:    567
# Dislikes: 0
# Total Accepted:    94.8K
# Total Submissions: 190.2K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
# 
# 示例:
# 
# 输入:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from typing import List
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            # 两个链表头部较小的一个与剩下元素的 merge 操作结果合并
            # 我们让l1保持为链表头部较小的那个链表
            if l1.val > l2.val: l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        while len(lists)>1:
            lists.insert(0, self.mergeTwoLists(lists.pop(),lists.pop()))
        return lists[0] if lists != [] else None
# @lc code=end
if __name__ == "__main__":
    print(len([]))

