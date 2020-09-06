# @before-stub-for-debug-begin
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=486 lang=python3
#
# [486] 预测赢家
#
from typing import *
# @lc code=start


class Solution:
    # 记忆搜索
    def memory_search(self, nums: List[int]) -> bool:
        total  = sum(nums)
        # 先手和第二个人能从numbers中获取的最大收益
        @lru_cache()
        def getMaxIncome(numbers): 
            if not numbers:
                return 0, 0
            if len(numbers) == 1:
                return numbers[0], 0
            # 尝试从左边或右边选取一个
            b, a = getMaxIncome(numbers[1:]) 
            d, c = getMaxIncome(numbers[:-1])
            ret = (numbers[0] + a, b) if numbers[0] + a >= numbers[-1] + c else (numbers[-1] + c, d)
            return ret

        a, b = getMaxIncome(tuple(nums))
        return a >= b

    def burte_force(self, nums:List[int]) -> bool:
        """递归暴力法，玩家为1，和-1，玩家为1时取最大项，玩家为-1时取最小项"""
        # 镜像对手问题，如果nums长度为偶数个，直接返回胜利
        if len(nums)%2 == 0:return True
        def recursion(L, R, flag):
            if L==R:return nums[L]*flag
            get_left=nums[L]*flag+recursion(L+1,R,-flag)
            get_right=nums[R]*flag+recursion(L,R-1,-flag)
            return max(get_left * flag, get_right * flag) * flag
            # return {
            #     1:max(get_left,get_right),
            #     -1:min(get_left,get_right)
            # }[flag]
        return recursion(0,len(nums)-1,1)>=0

    def dynamic_programing(self, nums: List[int]) -> bool:
        # 镜像对手问题，如果nums长度为偶数个，直接返回胜利
        if len(nums)%2 == 0:
            return True
        n = len(nums)

        dp = [[0] * n for _ in range(n)]
        for i, num in enumerate(nums):
            dp[i][i] = num
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        return dp[0][n - 1] >= 0

        # dp = nums.copy()
        # for i in range(n - 2, -1, -1):
        #     for j in range(i + 1, n):
        #         dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])
        # return dp[n - 1] >= 0


        # for l in range(1,n):
        #     for i in range(n - l):
        #         j = i + l
        #         dp[i] = max(nums[i] - dp[i + 1],nums[j] - dp[i])
        # return dp[0] >= 0

    def PredictTheWinner(self, nums: List[int]) -> bool:
        return {
            1:lambda nums:self.dynamic_programing(nums)
        }[1](nums)


# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.dynamic_programing([1, 5, 2,1, 5, 2, 3]))
