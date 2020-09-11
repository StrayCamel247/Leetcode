#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    #中心扩散法Spread From Center
    def spread(self, s, left, right):
        """
        left = right 的时候，此时回文中心是一条线，回文串的长度是奇数
        right = left + 1 的时候，此时回文中心是任意一个字符，回文串的长度是偶数
        """

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
   
    # manacher法专门用来解决回文字符串的问题
    def mancher(self, s:str) -> str:
        '''
        这是一个复杂度为 O(n) 的 Manacher 算法。
        假如字符串是奇数个，那么我们可以通过遍历所有字符串，再对所有字符串进行左右匹配，就像中心扩散方法一样。然后得到长度最大的字符串
        但是如果字符串是偶数个，我们无法进行此操作
        这个算法的最终要的额一点就是，我们将一个偶数长/奇数长的字符串，构造成新的字符串。
        这样我们可以对新字符串的每个字符，进行左右匹配。
        '''
        if len(s) < 2:
            return s
        # 将一个可能是偶数长/奇数长的字符串，首位以及每个字符间添加#
        test = '#'+'#'.join(s)+'#'
        print(test)
        # 当前遍历的中心最大扩散步数，其值等于原始字符串的最长回文子串的长度
        max_len = 0
        for i in range(len(test)):
            left = i - 1
            right = i + 1
            step = 0
            print(test[i])
            while left >= 0 and right < len(test) and test[left] == test[right]:
                print("spread",test[left],test[right])
                left -= 1
                right += 1
                step += 1
                print(step)
            
            if step > max_len:
                max_len = step
                start = (i - max_len) // 2
        return s[start: start + max_len]

    # 动态规划法-中心扩散法Spread From Center
    def spread_from_center(self, s:str) -> str:
        '''
        中心扩散法:
        为了改进暴力法，我们首先观察如何避免在验证回文时进行不必要的重复计算。考虑“ababa” 一定是回文，因为它的左首字母和右尾字母是相同的。
        我们给出 P(i,j) 的定义如下：
            如果子串S_i和S_j是回文字符串则P(i,j)为ture
            其他情况，P(i,j)为false
        因此   P(i,j)=(P(i+1,j−1) and S_i==S_j)
        基本示例如下：
            P(i, i) = true
            P(i, i+1) = ( S_i == S_{i+1} )
        这产生了一个直观的动态规划解法，我们首先初始化一字母和二字母的回文，然后找到所有三字母回文，并依此类推…
        复杂度分析
            时间复杂度：O(n^2)
            空间复杂度：O(1)
        '''
        
        if s==s[::-1]:
            print(s)
            return s
        res = s[:1]
        for i in range(len(s)):
            palindrome_odd= self.spread(s,i, i)
            palindrome_even= self.spread(s,i, i + 1)
            # 当前找到的最长回文子串
            res = max(palindrome_odd,palindrome_even,res,key=len)
        return res

    # 暴力法
    def force(self, s: str) -> str:
        '''
        很明显，暴力法将选出所有子字符串可能的开始和结束位置，并检验它是不是回文。
        时间复杂度：O(n^2),往往利用python的切片可以很好的缩减复杂度
        如果不用切片，还需要遍历一次子字符串，时间复杂度就是O(^3)
        空间复杂度：O(1)
        '''
        
        if s==s[::-1]:
            return s
        max_len = 1
        res = s[0]
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                if j - i + 1 > max_len and s[i:j+1] == s[i:j+1][::-1]:
                    max_len = j - i + 1
                    res = s[i:j + 1]
        return res
    def longestPalindrome(self, s: str) -> str:
        return{
            1 : lambda s:self.force(s),
            2 : lambda s:self.spread_from_center(s),
            3 : lambda s:self.mancher(s),
        }[3](s)
# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.longestPalindrome("abab"))
    # test= "test"
    # print('#'+'#'.join(test)+'#')