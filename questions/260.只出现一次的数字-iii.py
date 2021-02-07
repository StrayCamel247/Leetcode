#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] 只出现一次的数字 III
#
# https://leetcode-cn.com/problems/single-number-iii/description/
#
# algorithms
# Medium (73.63%)
# Likes:    354
# Dislikes: 0
# Total Accepted:    36.3K
# Total Submissions: 49.6K
# Testcase Example:  '[1,2,1,3,2,5]'
#
# 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。
# 
# 
# 
# 进阶：你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,1,3,2,5]
# 输出：[3,5]
# 解释：[5, 3] 也是有效的答案。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [-1,0]
# 输出：[-1,0]
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [0,1]
# 输出：[1,0]
# 
# 
# 提示：
# 
# 
# 2 
# -2^31 
# 除两个只出现一次的整数外，nums 中的其他数字都出现两次
# 
# 
#
from typing import List
import functools
# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # 进行累异或
        ret = functools.reduce(lambda x, y: x ^ y, nums)
        # 获取二进制结果中 最小为1的位，比如ret=10010 div为10
        div = 1
        while div & ret == 0:
            div <<= 1
        # if n & div 和 if not n & div 可以将两个不一样的数分出来，对进行分组后的数进行全员^，相同的数会被置为0，不同的数会被筛选出来，两组分组的数据全员异或的结果就分别是答案了
        a, b = 0, 0
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a, b]

# @lc code=end

