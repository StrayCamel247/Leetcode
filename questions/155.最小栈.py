#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#
# https://leetcode-cn.com/problems/min-stack/description/
#
# algorithms
# Easy (52.46%)
# Likes:    440
# Dislikes: 0
# Total Accepted:    90.9K
# Total Submissions: 173.3K
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n' + '[[],[-2],[0],[-3],[],[],[],[]]'
#
# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
# 
# 
# push(x) —— 将元素 x 推入栈中。
# pop() —— 删除栈顶的元素。
# top() —— 获取栈顶元素。
# getMin() —— 检索栈中的最小元素。
# 
# 
# 示例:
# 
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
# 
# 
#

# @lc code=start
class MinStack:

    # 辅助栈和数据栈不同步
    # 关键 1：辅助栈的元素空的时候，必须放入新进来的数
    # 关键 2：新来的数小于或者等于辅助栈栈顶元素的时候，才放入（特别注意这里等于要考虑进去）
    # 关键 3：出栈的时候，辅助栈的栈顶元素等于数据栈的栈顶元素，才出栈，即"出栈保持同步"就可以了

    def __init__(self):
        # 数据栈
        self.data = []
        # 辅助栈
        self._data = []

    def push(self, x):
        self.data.append(x)
        # 关键 1 和关键 2
        if len(self._data) == 0 or x <= self._data[-1]:
            self._data.append(x)

    def pop(self):
        # 关键 3：【注意】不论怎么样，数据栈都要 pop 出元素
        top = self.data.pop()

        if self._data and top == self._data[-1]:
            self._data.pop()
        return top

    def top(self):
        if self.data:
            return self.data[-1]

    def getMin(self):
        if self._data:
            return self._data[-1]




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

