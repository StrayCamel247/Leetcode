#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import typing


class ListNode():
    """本地编辑器使用的时候，请先将输入的对象转换成ListNode：head = ListNode(head)"""
    def __init__(self, val):
        if isinstance(val, int):
            self.val = val
            self.next = None

        elif isinstance(val, list):
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
    def Recursion(self, head: ListNode, n: int) -> ListNode:
        # NOTE:head = ListNode(head)
        global i
        if head is None:
            i = 0
            return None
        head.next = self.removeNthFromEnd(head.next, n)
        i += 1
        return head.next if i == n else head

    def string_concatenation(self, head: ListNode, n: int) -> ListNode:
        # NOTE:head = ListNode(head)
        prev = head
        s = "prev" + ".next"*n
        if eval(s) == None:  # 要删除的点是第一个节点
            return prev.next  # 删除第一个节点
        while eval(s+".next") != None:  # n+1个next，多往后找一个，以防止要删除的是最后一个
            prev = prev.next
        if prev.next != None:
            # prev.val = prev.next.val#这两行的代码相当于是删除当前节点那道题，如果只用n个.next的情况下
            prev.next = prev.next.next
        else:  # 删除的点是最后一个
            prev.next = None
        return head

    def traversing(self, head: ListNode, n: int) -> ListNode:
       # NOTE:head = ListNode(head)
        _list = []
        while head != None:
            _list.append(head.val)
            head = head.next
        del _list[-n]
        res = []
        for k, v in enumerate(_list):
            res.append(ListNode(v))
            if len(res) > 1:
                res[-2].next = res[-1]
        return res[0] if res else []

    def double_index(self, head: ListNode, n: int) -> ListNode:
        if not head:return head
        re = l = r = ListNode(0)
        r.next = head
        
        # 放置快指针
        while n+1:
            r = r.next
            n-=1

        # 快慢指针同时运行
        while r:
            l = l.next
            r = r.next
        l.next = l.next.next

        # 返回删除后的链表
        return re.next

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        return {
            1: lambda head, n: self.string_concatenation(head, n),
            2: lambda head, n: self.Recursion(head, n),
            3: lambda head, n: self.traversing(head, n),
            4: lambda head, n: self.double_index(head, n)
        }[4](head, n)


# @lc code=end
# if __name__ == "__main__":
#     test = Solution()
#     print(test.removeNthFromEnd([1, 2, 3, 4, 5], 2))
