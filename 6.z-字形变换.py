#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start

class Solution:

    def test(self, s: str, numRows: int) -> str:
        '''
        和二维数组的思想区别在于，我们我们可以将二维数组的行list，改为用字符串来存储。
        其实之后返回的值也是str所有用字符串可以更多地节省str-list-str的转换资源消耗

        首先构建numRows行的list用来存储数据
            这里每一列都是一个字符串形式
        假设 numRows为3，
            我们需要从res[0]到res[1]到2res[再]到1再res[0]到res[1]到res[2]的来存储字符串数据
这里我们需要定义flag，我们每访问完一次res[start]后：
        如果此时的start为第一行或者最后一行
            则对flag取相反数，转换顺序
            （我们开始 从0-1的访问时，可以先设置默认的flag为-1，当访问完res[0]后，取相反数，就是正方向了）
        '''
        
        if numRows < 2:
            return s
        res = ["" for i in range(numRows)]
        start, flag = 0, -1
        for c in s:
            # print(c)
            res[start] += c
            if start == 0 or start == numRows - 1: 
                flag = -flag
            start += flag
        # for i in range(numRows):
        #     print(res[i])
        return "".join(res)
    def test2(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        part = numRows*2-2
        print(part)
        print(len(s))
        a = len(s)//part +1
        test = list(s)
        res = [["" for i in range((numRows-1)*a)] for i in range(numRows)]
        # for i in res:
        #     print(i)
        print("a",a)
        n =0
        for j in range((numRows-1)*a):
            # print(j)
            if n ==  numRows -1 or n == 0:
                n = 0
                for i in range(numRows):
                    if test != []:
                        # print("字符串",test)
                        res[i][j] = test[0]
                        # for i in res:
                        #     print(i)
                        test.remove(test[0])
                        # print(res)
                n += 1
            else:
                if test != []:
                    # print("转折")
                    # print((numRows-1)*a)
                    # print(test[0])
                    res[numRows-1-n][j] = test[0]
                    # print(res[n][j])
                    test.remove(test[0])
                n +=1
        # for i in res:
        #     print(i)
        ans = ""
        for i in res:
            # print(i)
            for j in i :
                if j !='':
                    ans += j
                    # print(ans)
        
        return ans

    def convert(self, s: str, numRows: int) -> str:
        return {
            1: lambda s,numRows:self.test(s,numRows),
            2: lambda s,numRows:self.test2(s,numRows),
        }[1](s,numRows)

# @lc code=end

if __name__ == "__main__":
    pass
    # test = Solution()
    # print(test.convert("PAYPALISHIRING",3))
    


