#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''
# @lc code=start
import random
from typing import List
class Solution:
    type = random.randint(1,2)
    def force(self, nums: List[int], target: int) -> List[int]:
        '''
        暴力法：遍历每个元素 x，并查找是否存在一个值与 target− 相等的目标元素。
        如果采用传统的两遍遍历：
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if target == nums[i] + nums[j]:
                        return [i,j]
                    else:
                        return []
            时间复杂度：O(n^2)
            空间复杂度：O(1)
        采用切片：
            当第二次遍历的时候，我们可以采用python的切片list[x:y]来重组第i个数据及其以后的数据
            再通过判断if (target - nums[i]) in nums[i:]来解答
        '''
        print("当前使用的暴力破解的方法\n")
        n=0
        for i in range(0,len(nums)-1):
            # print(nums[i+1:])
            # print(nums[i])
            n+=1
            if (target - nums[i]) in nums[i+1:]:
                return [i,nums[i+1:].index(target - nums[i])+n]
            
    def hash_map(self, nums: List[int], target: int) -> List[int]:
        '''
        通过以空间换取速度的方式，我们可以将查找时间从 O(n) 降低到 O(1)。哈希表正是为此目的而构建的，它支持以近似恒定的时间进行快速查找。
        我用“近似”来描述，是因为一旦出现冲突，查找用时可能会退化到 O(n)。
        但只要你仔细地挑选哈希函数，在哈希表中进行查找的用时应当被摊销为 O(1)。

        一个简单的实现使用了两次迭代。
        在第一次迭代中，我们将每个元素的值和它的索引添加到表中。
        在第二次迭代中，我们将检查每个元素所对应的目标元素（target - nums[i]target−nums[i]）是否存在于表中。
        注意，该目标元素不能是 nums[i] 本身！

        时间复杂度：O(n)
        我们把包含有 n个元素的列表遍历两次。由于哈希表将查找时间缩短到 O(1)
        空间复杂度：O(n)
        所需的额外空间取决于哈希表中存储的元素数量，该表中存储了 n 个元素
        '''
        print("当前使用的哈希表方法\n")
        hashmap={}
        for i,n in enumerate(nums):
            if target - n in hashmap:
                return [hashmap.get(target - n),i]
            hashmap[n] = i



    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # print('type',self.type)
        return {
            1 : lambda nums,target : self.force(nums,target),
            2 : lambda nums,target : self.hash_map(nums,target),
        }[2](nums,target)

# @lc code=end

if __name__ == "__main__":
    pass