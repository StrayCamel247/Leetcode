#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
import bisect
from typing import List
# @lc code=start


class Solution:
    def __init__(self):
        self.result = []

    def classic_double_index(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        if len(nums) < 4:
            return []
        """双指针"""
        for k, v in enumerate(nums[:-3]):
            # 当数组最小值和都大于target 跳出
            if v*4 > target:
                break
            # 当数组最大值和都小于target或者已经遍历过，遍历下一个
            if v + 3*nums[-1] < target or (v == nums[k-1] and k>0):
                continue
            for _k, _v in enumerate(nums[k+1:-2], k+1):
                # 同理
                if v + _v*3 > target:
                    break
                if v + _v + nums[-1]*2 < target or (_v == nums[_k-1] and _k>k+1):
                    continue
                R = len(nums)-1
                L = max(_k + 1, bisect.bisect_left(nums,
                                                   target-nums[R] - _v - v, _k + 1, R) - 1)
                while L < R:
                    _sum = v+_v+nums[L]+nums[R]
                    if _sum == target:
                        self.result.append(
                            tuple(sorted((v, _v, nums[L], nums[R]))))
                        L = bisect.bisect_right(nums, nums[L], L, R)
                        R = bisect.bisect_left(nums, nums[R], L, R)-1
                    else:
                        L, R = L+(_sum < target), R-(_sum > target)
        return [list(_) for _ in set(self.result)]
    
    def brute_for(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        if len(nums) < 4:
            return []
        counter={}
        for n in nums:
            counter[n]=counter.get(n,0)+1
        """双指针"""
        for k, v in enumerate(nums[:-3]):
            # 当数组最小值和都大于target 跳出
            if v*4 > target:
                break
            # 当数组最大值和都小于target或者已经遍历过，遍历下一个
            if v + 3*nums[-1] < target or (v == nums[k-1] and k>0):
                continue
            counter[v]-=1
            for _k, _v in enumerate(nums[k+1:-2], k+1):
                # 同理
                if v + _v*3 > target:
                    break
                if v + _v + nums[-1]*2 < target or (_v == nums[_k-1] and _k>k+1):
                    continue
                counter[_v]-=1
                for __k in range(_k if counter[_v]>0 else _k+1,len(nums)):
                    c=nums[__k]
                    d=target-v-_v-c
                    if c>d:
                        break
                    if d not in counter or c==d and counter[c]<2:
                        continue
                    self.result.append((v,_v,c,d))
                counter[_v]+=1
        return [list(_) for _ in set(self.result)]

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        return {
            1: lambda nums, target: self.classic_double_index(nums, target),
            2: lambda nums, target: self.brute_for(nums, target),
        }[2](nums, target)


# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.fourSum([0,0,0,0], 0))
