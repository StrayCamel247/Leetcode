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
        
        self.other_G = [
            ['', 'M', 'MM', 'MMM'],
            ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
            ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
            ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        ]

    def other(self, num:int) -> str:
        d = [1000, 100, 10, 1]
        r = ''
        for k, v in enumerate(d):
            r += self.other_G[k][int(num/v)]
            num = num % v
        return r

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
            2:lambda num:self.other(num),
        }[2](num)
# @lc code=end

if __name__ == "__main__":
    solve = Solution()
    # print(solve.Glossary.items())
    print(solve.intToRoman(90))