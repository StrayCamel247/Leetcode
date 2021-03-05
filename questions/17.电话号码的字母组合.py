#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
from typing import List
# @lc code=start
import itertools
class Solution:
    def __init__(self):
        super().__init__()
        # self.num_char_dict = {str(k):v for k,v in enumerate(['abc','def','ghi','jkl','mno','pqr','stuv','wxyz'], 2)}
        self.num_char_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        self.res = ['']
    # BFS,宽度优先
    def pythonic(self, digits: str) -> List[str]:
        if not digits: return []
        for digit in digits:
            self.res = [r+char for r in self.res for char in self.num_char_dict[digit]]
        return self.res
    def dfs(self, digits: str) -> List[str]:
        if not digits: return []
        # Back Tracking Method,回溯法
        def backtrack(conbination,nextdigit):
            if len(nextdigit) == 0:
                self.res.append(conbination)
            else:
                for letter in self.num_char_dict[nextdigit[0]]:
                    backtrack(conbination + letter,nextdigit[1:])
        self.res = []
        backtrack('',digits)
        return self.res

    def letterCombinations(self, digits: str) -> List[str]:
        return {
            1: lambda digits: self.pythonic(digits),
            2: lambda digits: self.dfs(digits),
        }[2](digits)
# @lc code=end

