#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (61.86%)
# Likes:    433
# Dislikes: 0
# Total Accepted:    103.4K
# Total Submissions: 167K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
# 
# 示例 1:
# 
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 
# 
# 示例 2:
# 
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
# 
# 说明: 
# 
# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
# 
#

# @lc code=start
from typing import List
import heapq
import random
# 排序法 -> 小根堆 -> 快排划分法 -> BFPRT算法
class Solution:
    # 二分法查找
    def erfen_test(self, nums: List[int], k: int) -> int:
        # 使用一个长度为k的小数组存储前k个元素（大小）；
        # 遍历数组，使用二分法查找小数组中第一个比当前元素小的数
        ans = [float('-inf') for i in range(k)]

        for i in nums:
            # 如果当前元素小于等于数组中最小的元素
            if ans[0] >= i:
                continue
            # 如果当前元素大于等于数组中最大的元素
            if ans[-1] <= i:
                ans = ans[1:] + [i]
                continue

            # 二分法定位要插入的位置    
            l = 0
            r = k - 1
            while l < r:
                m = (l + r) // 2

                # 如果i <= ans[m]，则需要插入的位置一定在m的左边，不包括m
                if i <= ans[m]:
                    r = m - 1
                # 如果i > ans[m]并且i小于m的下一个元素，则插入的位置在m
                elif ans[m + 1] >= i:
                    l = m
                    break
                # 插入的位置在m之后，不包括m
                else:
                    l = m + 1
            # 新的前k元素数组
            ans = ans[1:l + 1] + [i] + ans[l + 1:]
        return ans[0]

    # 自带的sort
    def sort_test(self, nums: List[int], k: int) -> int:
        # 普通的sort()方法
        # 时间复杂度O(N*logN),空间复杂度O(1)
        nums.sort()
        return nums[-k]
    
    # 创建小顶堆, k长的堆中插入数据的时间复杂度为logk，总共需要插入n个数据所以时间复杂度为nlogk
    def findKthLargest(self, nums: List[int], k: int) -> int:
        print()
        return heapq.nlargest(k, nums)[-1]
    
    # 快排
    def quicksort(self, nums: List[int], k: int) -> int:
        """
        改进的快排，平均时间复杂度为 {O}(N)O(N)
        这样，在输出的数组中，枢轴达到其合适位置。所有小于枢轴的元素都在其左侧，所有大于或等于的元素都在其右侧。

        这样，数组就被分成了两部分。如果是快速排序算法，会在这里递归地对两部分进行快速排序，时间复杂度为 {O}(N \log N)O(NlogN)。

        而在这里，由于知道要找的第 N - k 小的元素在哪部分中，我们不需要对两部分都做处理，这样就将平均时间复杂度下降到 {O}(N)O(N)。
        """

        def quick_sort(left, right, nums):
            l, r = left, right
            index = randint(l, r)
            nums[l], nums[index] = nums[index], nums[l]
            while l < r:
                while l < r:
                    if nums[r] < nums[l]:
                        nums[l], nums[r] = nums[r], nums[l]
                        l += 1
                        while l < r:
                            if nums[l] > nums[r]:
                                nums[l], nums[r] = nums[r], nums[l]
                                r -= 1
                                break
                            else:
                                l += 1
                    else:
                        r -= 1
            # 当快排的基数的index也就是l等于我们要找的第k个的时候，返回
            if l == len(nums) - k:
                return nums[l]
            # 当快排的基数的index也就是大于我们要找的第k个的时候，继续快排，但是缩小范围到left, l - 1
            elif l > len(nums) - k:
                return quick_sort(left, l - 1, nums)
            # 当快排的基数的index也就是大于我们要找的第k个的时候，继续快排，但是缩小范围到l + 1, right
            else:
                return quick_sort(l + 1, right, nums)

        return quick_sort(0, len(nums) - 1, nums)


# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.findKthLargest([3,2,1,5,6,4],2))
    print(test.quicksort([3,2,1,5,6,4],2))
