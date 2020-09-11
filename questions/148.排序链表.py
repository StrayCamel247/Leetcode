#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
# https://leetcode-cn.com/problems/sort-list/description/
#
# algorithms
# Medium (64.81%)
# Likes:    489
# Dislikes: 0
# Total Accepted:    53K
# Total Submissions: 81.7K
# Testcase Example:  '[4,2,1,3]'
#
# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
# 
# 示例 1:
# 
# 输入: 4->2->1->3
# 输出: 1->2->3->4
# 
# 
# 示例 2:
# 
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5
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
    def __init__(self):
        self.flag = 0
    # 题目要求时间空间复杂度分别为O(nlogn)和O(1)，根据时间复杂度我们自然想到二分法，从而联想到归并排序；https://leetcode-cn.com/problems/sort-list/solution/sort-list-gui-bing-pai-xu-lian-biao-by-jyd/
    def sortList(self, head: ListNode) -> ListNode:
        # print(head)
        # print(self.flag)
        self.flag += 1
        if not head or not head.next: return head 
        slow, fast = head, head.next
        # 使用二分法我们必须要找到链表的中点
        # 设计快慢指针，快指针走两步，慢指针走一步，当fast走到结尾，slow的位置就是中点
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        # 找到中点，并使用slow.next = None截断链表
        mid, slow.next = slow.next, None
        # self.sortList(head), self.sortList(mid)分别为mid节点左右的两端list
        left, right = self.sortList(head), self.sortList(mid)
        # 合并 merge 环节： 将两个排序链表合并，转化为一个排序链表,利用双指针
        tmp = res = ListNode(0)
        while left and right:
            # print('left, right', left, right)
            if left.val < right.val: tmp.next, left = left, left.next
            else: tmp.next, right = right, right.next
            tmp = tmp.next
            # print('res', res)
        tmp.next = left if left else right
        return res.next
# @lc code=end
if __name__ == "__main__":
    print(Solution().sortList(ListNode([4,2,1,3])))
