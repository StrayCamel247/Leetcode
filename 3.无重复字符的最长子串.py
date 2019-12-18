#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def check_str(self,s: str) -> bool:
        for i in range(len(s)):
            if s[i] in s[i+1:]:
                return False
        return True
    # 暴力法
    def force(self, s: str) -> int:
        '''
        暴力法：
        我们可以遍历给定字符串 s 的所有可能的子字符串并判断子字符串是否有无重复。 
        如果没有重复，那么我们将会更新无重复字符子串的最大长度的答案。
        时间复杂度：O(n^3)
            要验证索引范围在 [i, j) 内的字符是否都是唯一的，我们需要检查该范围中的所有字符
            对于所有 j∈[i+1,n] 所耗费的时间总和为：i+1∑n O(j−i)
                对于给定的 i∈[0,n-1]
                因此时间复杂度为O(n^3)
        空间复杂度O(n)
        '''
        m=0
        if s != "":
            m=1
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i] != s[j]:
                    if self.check_str(s[i:j+1]):
                        m = max(m,len(s[i:j+1]))
        return m
    # 窗口滑动法
    def sliding_window(self, s: str) -> int:
        '''
        在暴力法中，我们会反复检查一个子字符串是否含有有重复的字符，但这是没有必要的。
        如果从索引 i 到 j - 1之间的子字符串 s[i:j]已经被检查为没有重复字符。我们只需要检查 s[j] 对应的字符是否已经存在于子字符串s[i:j]中。
        要检查一个字符是否已经在子字符串中，我们可以检查整个子字符串，这将产生一个复杂度为 O(n^2)的算法，但我们可以做得更好。

        通过使用 HashSet 作为滑动窗口，我们可以用 O(1)的时间来完成对字符是否在当前的子字符串中的检查。
        滑动窗口是数组/字符串问题中常用的抽象概念。 
        窗口通常是在数组/字符串中由开始和结束索引定义的一系列元素的集合，即s[i,j).add()而滑动窗口是可以将两个边界向某一方向“滑动”的窗口。例如，我们将 [i, j)向右滑动 1 个元素，则它将变为 [i+1, j+1)（左闭，右开）。

        回到我们的问题，我们使用 HashSet 将字符存储在当前窗口 [i, j)（最初 j = i）中。 然后我们向右侧滑动索引 j，如果它不在 HashSet 中，我们会继续滑动 j。直到 s[j] 已经存在于 HashSet 中。此时，我们找到的没有重复字符的最长子字符串将会以索引 i 开头。如果我们对所有的 i 这样做，就可以得到答案。

        时间复杂度：O(2n) = O(n)O，在最糟糕的情况下，每个字符将被 i 和 j 访问两次。

        空间复杂度：O(min(m, n))，与之前的方法相同。滑动窗口法需要 O(k) 的空间，其中 k 表示 Set 的大小。而 Set 的大小取决于字符串 n 的大小以及字符集 / 字母 m 的大小。

        '''
        # 
        dic = {}
        # 定义窗口左边和最大无重复子字符串长度为0
        i ,res = 0, 0
        # 向右从0依次滑动窗口右边j
        for j in range(len(s)):
            # 当窗口中的字符串有重复
            if s[j] in dic:
                #将窗口左边i向后移动
                i = max(dic[s[j]], i)
                # i +=1
            # 获取新的最大无重复子字符串长度
            res = max(res, j-i+1)
            # 将j滑过的字符存入dic
            dic[s[j]] = j+1
        return res
    def test(self, s:str) -> int:
        length,j = 0,-1
        for i,x in enumerate(s):
            if x in s[j+1:i]:
                length = max(length,i-j-1)
                j = s[j+1:i].index(x)+j+1
        return max(length,len(s)-1-j)
        
    def lengthOfLongestSubstring(self, s: str) -> int:
        return {
            1 : lambda s : self.force(s),
            2 : lambda s : self.sliding_window(s),
            3 : lambda s : self.test(s)
        }[3](s)

    
# @lc code=end

if __name__ == "__main__":
    pass
    # test = Solution()
    # print(test.lengthOfLongestSubstring("9999"))
    # if test.check_str("godk"):
    #     print("s")
    # else:
    #     print('g')