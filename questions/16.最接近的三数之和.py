#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
from typing import List
import bisect
# @lc code=start


class Solution:
    """和三数之和为0的思路一样，使用双指针设计思路如下：排序；遍历"""

    def __init__(self):
        self.res = float('inf')

    def classic_double_index(self, nums: List[int], target: int) -> int:
        nums.sort()
        if len(nums) == 3:
            return sum(nums)
        for k, v in enumerate(nums[:-2]):
            if k > 0 and v == nums[k-1]:
                continue
            L, R = k+1, len(nums)-1
            if sum(nums[k:k+3]) > target:
                self.res = sum(nums[k:k+3]) if abs(sum(nums[k:k+3]) -
                                                   target) < abs(self.res - target) else self.res
                break
            if sum(nums[-2:], nums[k]) < target:
                self.res = sum(nums[-2:], nums[k]) if abs(sum(nums[-2:],
                                                              nums[k]) - target) < abs(self.res - target) else self.res
                continue
            while L < R:
                _sum = v+nums[L]+nums[R]
                if _sum == target:
                    return _sum
                if abs(_sum-target) < abs(self.res-target):
                    self.res = _sum
                # self.update(_sum, target)
                if _sum > target:
                    _R = R - 1
                    # 移动到下一个不相等的元素
                    while L < _R and nums[_R] == nums[R]:
                        _R -= 1
                    R = _R
                else:
                    _L = L + 1
                    # 移动到下一个不相等的元素
                    while _L < R and nums[_L] == nums[L]:
                        _L += 1
                    L = _L
        return self.res

    def classic_double_index_v2(self, nums: List[int], target: int) -> int:
        nums.sort()
        if len(nums) == 3:
            return sum(nums)
        for k, v in enumerate(nums[:-2]):
            R = len(nums)-1
            L = max(k + 1, bisect.bisect_left(nums,
                                              target-nums[R] - nums[k], k + 1, R) - 1)
            while self.res != target and L < R:
                _sum = v+nums[L]+nums[R]
                self.res, L, R = min(self.res, _sum, key=lambda x: abs(
                    x - target)), L + (_sum < target), R - (_sum > target)
        return self.res

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        return {
            1: lambda nums, target: self.classic_double_index(nums, target),
            2: lambda nums, target: self.classic_double_index_v2(nums, target),
        }[2](nums, target)


        # while nums[L] == nums[L+1] :
        #     L = L+1
        # while nums[R] == nums[R-1] :
        #         R = R-1
# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.threeSumClosest([1, 1, 1, 1], 0))
