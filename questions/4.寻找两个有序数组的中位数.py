#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#

# @lc code=start
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        len1, len2 = len(nums1), len(nums2)
        
        left, right, half_len = 0, len1, (len1 + len2 + 1) // 2
        mid1 = (left + right) // 2
        mid2 = half_len - mid1
        
        while left < right:
            if mid1 < len1 and nums2[mid2-1] > nums1[mid1]:
                left = mid1 + 1
            else:
                right = mid1
            mid1 = (left + right) // 2
            mid2 = half_len - mid1
        
        if mid1 == 0: 
            max_of_left = nums2[mid2-1]
        elif mid2 == 0: 
            max_of_left = nums1[mid1-1]
        else: 
            max_of_left = max(nums1[mid1-1], nums2[mid2-1])

        if (len1 + len2) % 2 == 1:
            return max_of_left

        if mid1 == len1: 
            min_of_right = nums2[mid2]
        elif mid2 == len2: 
            min_of_right = nums1[mid1]
        else: 
            min_of_right = min(nums1[mid1], nums2[mid2])

        return (max_of_left + min_of_right) / 2
    def test(self, nums1: List[int], nums2: List[int]) -> float:

        num=sorted(nums1+nums2)
        lens=len(num)
        print(num, lens)
        print(lens//2, (lens-1)//2)
        return((num[lens//2]+num[(lens-1)//2])/2)




# @lc code=end

if __name__ == "__main__":
    test = Solution()
    print(test.findMedianSortedArrays([1, 2], [3,2,2,3,3,3,4]))
