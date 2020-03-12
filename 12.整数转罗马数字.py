#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def __init__(self):
        self.Glossary = [
            ['I','V','X'],
            ['X','L','C'],
            ['C','D','M'],
            ['M'],
        ]
    def viaDict(self, num:int) -> str:
        resl,nlist=[],list(str(num))
        for k,v in enumerate(self.Glossary):
            try:
                _,res,x=0,'',int(nlist.pop())
                while _<x:
                    res+=v[0]
                    _+=1
                    if _==4:
                        res=v[0]+v[1]
                    elif _==5:
                        res=v[1]
                    elif _==9:
                        res=v[0]+v[2]
                resl.insert(0,res)
            except (StopIteration,IndexError):
                # 遇到StopIteration就退出循环
                break
        return "".join(resl)
    def intToRoman(self, num: int) -> str:
        return {
            1:lambda num:self.viaDict(num),
        }[1](num)
# @lc code=end

if __name__ == "__main__":
    solve = Solution()
    # print(solve.Glossary.items())
    print(solve.intToRoman(90))