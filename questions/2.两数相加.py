#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''
# @lc code=start
# Definition for singly-linked list.
# class ListNode():
#     def __init__(self, val):
#         if isinstance(val,int):
#             self.val = val
#             self.next = None
            
#         elif isinstance(val,list):
#             self.val = val[0]
#             self.next = None
#             cur = self
#             for i in val[1:]:
#                 cur.next = ListNode(i)
#                 cur = cur.next
    
#     def gatherAttrs(self):
#         return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

#     def __str__(self):
#             return self.__class__.__name__+" {"+"{}".format(self.gatherAttrs())+"}"


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        re = ListNode(0)
        r=re
        carry=0
        while(l1 or l2):
            x= l1.val if l1 else 0
            y= l2.val if l2 else 0
            s=carry+x+y
            carry=s//10
            r.next=ListNode(s%10)
            r=r.next
            if(l1!=None):l1=l1.next
            if(l2!=None):l2=l2.next
        if(carry>0):
            r.next=ListNode(1)
        return re.next
# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.addTwoNumbers(ListNode([2,4,3]),ListNode([5,6,4])))