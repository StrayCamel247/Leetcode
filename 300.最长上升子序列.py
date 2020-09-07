#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#
from typing import List
# @lc code=start
class Solution:
    def __init__(self):
        super().__init__()
        self._dict = {}
    def grid_dp(self, nums: List[int]) -> int:
        # 动态规划
        grid = [1 for _ in nums]
        # grid = [max(grid[k], grid[_k]+1) for _k,_v in enumerate(nums[:k]) for k,v in enumerate(nums) if v>_v]
        for k,v in enumerate(nums):
            for _k,_v in enumerate(nums[:k]):
                if v>_v:
                    grid[k] = max(grid[k], grid[_k]+1)
        return max(grid)

    def lru_cache_recursion(self, nums:List[int]):
        import functools
        self._dict = {}
        @functools.lru_cache(None)
        def test(k):
            self._dict[k] = 1
            for _ in range(k,-1,-1):
                if nums[k]>nums[_]:
                    self._dict[k] = max(self._dict.get(k), self._dict.get(_, test(_))+1)
            if k >1:test(k-1)
        test(len(nums)-1)
        return max(self._dict.values())
            
    def Greedy_binary_search(self, nums: List[int]) -> int:
        # 贪心+二分查找
        # 时间复杂度：O(nlogn)。数组 nums 的长度为 n，我们依次用数组中的元素去更新 d 数组，而更新 d 数组时需要进行 O(logn) 的二分搜索，所以总时间复杂度为 O(nlogn)。
        # Accepted
        # 24/24 cases passed (44 ms)
        # Your runtime beats 98.77 % of python3 submissions
        # Your memory usage beats 9.92 % of python3 submissions (13.9 MB)
        d = []
        import bisect
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                l, r = 0, len(d) - 1
                loc = r
                idx = bisect.bisect_left(d,n)
                d[idx] = n
                # print(idx)
                # while l <= r:
                #     mid = (l + r) // 2
                #     if d[mid] >= n:
                #         loc = mid
                #         r = mid - 1
                #     else:
                #         l = mid + 1
                # d[loc] = n
        return len(d)

    def lengthOfLIS(self, nums: List[int]) -> int:
        # 动态规划
        return {
            1:lambda nums:self.lru_cache_recursion(nums),
            2:lambda nums:self.grid_dp(nums),
            3:lambda nums:self.Greedy_binary_search(nums)
        }[3](nums)
# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.lengthOfLIS([10,11,12,13,1,2,3]))
