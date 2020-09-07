#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

import functools
# @lc code=start
class Solution:
    def dp_brute(self,text1,text2):
        m, n = len(text1), len(text2)
        # 构建 DP table 和 base case
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # 进行状态转移
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    # 找到一个 lcs 中的字符
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]

    def lru_cache_recursion(self, text1, text2):
        # 递归动态规划，和暴力法差不多
        @functools.lru_cache(None)
        def test(i,j):
            if i == -1 or j == -1:
                return 0 
            if text1[i] == text2[j]:
                return test(i-1, j-1)+1
            else:
                return max(test(i-1, j), test(i, j-1))
        # i 和 j 初始化为最后一个索引
        return test(len(text1)-1, len(text2)-1)

    def greedy_binary_insert(self,text1,text2):
        # Accepted
        # 43/43 cases passed (64 ms)
        # Your runtime beats 99.92 % of python3 submissions
        # Your memory usage beats 94.06 % of python3 submissions (14.1 MB)
        import collections, bisect
        d = collections.defaultdict(list)
        for i in range(len(text2)-1, -1, -1):
            d[text2[i]].append(i)
        nums = []
        print(d)
        for c in text1:
            if c in d:
                nums.extend(d[c])
        print(nums)
        ans = []
        for num in nums:
            idx = bisect.bisect_left(ans, num)
            print(ans,num,idx)
            if idx == len(ans):
                ans.append(num)
            else:
                ans[idx] = num
        return len(ans)

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return {
            1:lambda text1,text2:self.lru_cache_recursion(text1,text2),
            2:lambda text1,text2:self.greedy_binary_insert(text1,text2),
            3:lambda text1,text2:self.dp_brute(text1,text2)
        }[2](text1,text2)

# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.longestCommonSubsequence('abddc3', '1a2b3c33333'))
