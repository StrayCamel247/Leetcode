#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
from typing import List

import copy
class Solution:
    def __init__(self):
        self.res = set()
        self.chr = ''
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(tmp,n):
            self.res = set()
            tmp1 = copy.deepcopy(list(tmp))
            n -= 1
            for _ in range(len(list(tmp))+1):
                tmp1.insert(_, '()')
                # tmp2 = copy.deepcopy(tmp1)
                r = ''.join(tmp1)
                self.res.add(r)
                tmp2 = copy.deepcopy(r)
                if n:dfs(tmp2, n)
        dfs('',n)
        print(self.res)

       
# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.generateParenthesis(2))
    # test = list('()')
    # for i in range(3):
    #     tmp1 = test
    #     for _ in range(len(test)+1):
    #         tmp1.insert(_,'()')
            
