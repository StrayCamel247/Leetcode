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

    def dfs_chr(self, tmp: str, n: int):
        n -= 1
        for _ in range(len(tmp)+1):
            # 每次循环都需要重新copy一下tmp
            tmp1 = copy.copy(list(tmp))
            tmp1.insert(_, '()')
            r = ''.join(tmp1)
            tmp2 = copy.copy(r)
            if n:
                self.dfs_chr(tmp2, n)
            else:
                self.res.add(r)
    
    
    def generateParenthesis(self, n: int) -> List[str]:
        self.dfs_chr(self.chr, n)
        # print(self.res)
        return list(self.res)

       
# @lc code=end
if __name__ == "__main__":
    test = Solution()
    test.generateParenthesis(3)

    # print(test.generateParenthesis(2))
    
    # print(test.id,test2.id)
    # for i in range(3):
    #     tmp1 = test
    #     for _ in range(len(test)+1):
    #         tmp1.insert(_,'()')
            
