#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
from typing import List
class Solution:
    def __init__(self):
        self.res = []
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if (not nums or len(nums)<3): return []
        nums.sort()
        print(nums)
        for i,v in enumerate(nums):
            if (v > 0):
                return self.res
            if (i>0 and v ==nums[i-1]):
                continue
            L=i+1
            R=len(nums)-1
            while(L<R):
            # 定义双指针，L,R指向的数和数V进行加和，判断大小并决定L,R指针向哪边移动
                if (v +nums[L]+nums[R]==0):
                    self.res.append([v ,nums[L],nums[R]])
                    # 当遇到L,R让三个数字和为0，如果L,R临近的点是重复的就先移动的重复的那个指针，如果没有就一起移动L,R，若不一起移动，单移动一边无法创造三个数和为0
                    while(L<R and nums[L]==nums[L+1]):
                        L=L+1
                    while(L<R and nums[R]==nums[R-1]):
                        R=R-1
                    L=L+1
                    R=R-1
                elif(v +nums[L]+nums[R]>0):
                    R=R-1
                else:
                    L=L+1
        return self.res

# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.threeSum([-1, 0, 1, 2, -1, -4]))