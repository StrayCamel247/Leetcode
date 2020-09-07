#
# @lc app=leetcode.cn id=354 lang=python3
#
# [354] 俄罗斯套娃信封问题
#
from typing import List
import bisect
# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # 题目和300题没啥区别
        # Accepted
            # 85/85 cases passed (192 ms)
            # Your runtime beats 78.21 % of python3 submissions
            # Your memory usage beats 81.38 % of python3 submissions (15.8 MB)
        if not envelopes:return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        _list = [i[1] for i in envelopes]
        for i in range(len(_list)):
            idx = bisect.bisect_left(dp, _list[i])
            if idx == len(dp):
                dp.append(_list[i])
            else:
                dp[idx] = _list[i]
        return len(dp)

# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
