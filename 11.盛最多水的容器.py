#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
from typing import List

class Solution:
    def __init__(self):
        self.maxContent = 0

    def burte_force(self, height: List[int]) -> int:
        # print(len(height))
        # get the last one & del it
        last = height.pop()
        for key,value in enumerate(height):
            # Short board effect, get the minimm value between the last one & current value
            tmp = min(last,value)*(len(height)-key)
            self.maxContent = max(tmp,self.maxContent)
            # print(self.maxContent)
        if len(height) == 1:
            return self.maxContent
        else:
            #Iterativly call self.burte_force() with new params height
            return(self.burte_force(height))
    
    def double_pointer(self, height: List[int]) -> int:
        i, j= 0, len(height) - 1
        while i < j:
            # the pointers approach eacher other, their distance becomes smaller, so the only when the short one approach the long one the area can be larger.
            if height[i] < height[j]:
                self.maxContent = max(self.maxContent, height[i] * (j - i))
                # the left pointer move right
                i += 1
            else:
                self.maxContent = max(self.maxContent, height[j] * (j - i))
                # the right pointer move left
                j -= 1
        return self.maxContent
    def maxArea(self, height: List[int]) -> int:
        return {
            0 :lambda height :self.burte_force(height),
            1 :lambda height :self.double_pointer(height),
        }[1](height)
# @lc code=end

if __name__ == "__main__":
    solve = Solution()
    print(solve.maxArea([1,8,6,2,5,4,8,3,7]))