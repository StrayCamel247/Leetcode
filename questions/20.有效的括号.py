#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def __init__(self):
        self.stack = []
        self.punctuation = {
            '{':'}',
            '(':')',
            '[':']',
        }
    def brute(self, s):
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''

    def validViaStack(self, s):
        # while s:
        #     if s[0] in self.punctuation:
        #         self.stack, s = self.stack+[s[0]], s[1:]
        #     elif not self.stack or self.punctuation[self.stack.pop()] is not s[0]:
        #         return False
        #     else:
        #         s = s[1:]

        for _ in s:
            if _ in self.punctuation:
                self.stack.append(_)
            elif not self.stack or self.punctuation[self.stack.pop()] is not _:
                    return False
        # 栈为空的时候退出
        return True if not self.stack else False

    def isValid(self, s):
        return self.validViaStack(s)
# @lc code=end
if __name__ == "__main__":
    test =Solution()
    # a = []
    t = '(){'
    # a , t = a+[t[0]], t[1:]
    print(test.validViaStack('{[]}'))
    # t = '()'
    # print(a,t)

