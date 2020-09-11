#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (60.83%)
# Likes:    944
# Dislikes: 0
# Total Accepted:    225.7K
# Total Submissions: 370.3K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 示例：
# 
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode():
    def __init__(self, val):
        if isinstance(val,int):
            self.val = val
            self.next = None
            
        elif isinstance(val,list):
            self.val = val[0]
            self.next = None
            cur = self
            for i in val[1:]:
                cur.next = ListNode(i)
                cur = cur.next
    
    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
            return self.__class__.__name__+" {"+"{}".format(self.gatherAttrs())+"}"

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        print(l1,l2)
        if l1 and l2:
            # 两个链表头部较小的一个与剩下元素的 merge 操作结果合并
            # 我们让l1保持为链表头部较小的那个链表
            if l1.val > l2.val: l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2
# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.mergeTwoLists(ListNode([1,2,4]), ListNode([1,3,4])))
