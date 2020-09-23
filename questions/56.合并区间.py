#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
# https://leetcode-cn.com/problems/merge-intervals/description/
#
# algorithms
# Medium (43.02%)
# Likes:    602
# Dislikes: 0
# Total Accepted:    143K
# Total Submissions: 332.3K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# 给出一个区间的集合，请合并所有重叠的区间。
#
#
#
# 示例 1:
#
# 输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#
#
# 示例 2:
#
# 输入: intervals = [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
#
# 注意：输入类型已于2019年4月15日更改。 请重置默认代码定义以获取新方法签名。
#
#
#
# 提示：
#
#
# intervals[i][0] <= intervals[i][1]
#
#
#
from typing import List
# @lc code=start


class Solution:
    def reversion(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals.sort(key=lambda x: x[0])
        left = self.merge(intervals[:len(intervals)//2])
        right = self.merge(intervals[len(intervals)//2:])
        for _ in range(len(right)-1, -1, -1):
            if left[-1][1] >= right[_][1]:
                return left+right[_+1:] if [right[_+1:]][0] else left
            elif left[-1][1] >= right[_][0]:
                left[-1][1] = right[_][1]
                return left+right[_+1:] if [right[_+1:]][0] else left

        return left+right

    def traverse(self, intervals: List[List[int]]) -> List[List[int]]:
        # 排序，一遍遍历
        if not intervals:
            return []
        ans = []
        intervals.sort()
        for num in intervals:
            if not ans or ans[-1][1] < num[0]:
                ans.append(num)
            elif ans[-1][1] >= num[0]:
                ans[-1][1] = max(ans[-1][1], num[1])
        return ans

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        return {
            1: lambda intervals: self.reversion(intervals),
            2: lambda intervals: self.traverse(intervals)
        }[2](intervals)

# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.merge([[1,3],[2,6],[8,10],[15,18]]))
