#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#
# https://leetcode-cn.com/problems/permutation-sequence/description/
#
# algorithms
# Medium (48.46%)
# Likes:    217
# Dislikes: 0
# Total Accepted:    29.2K
# Total Submissions: 60.3K
# Testcase Example:  '3\n3'
#
# 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
# 
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
# 
# 
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 
# 
# 给定 n 和 k，返回第 k 个排列。
# 
# 说明：
# 
# 
# 给定 n 的范围是 [1, 9]。
# 给定 k 的范围是[1,  n!]。
# 
# 
# 示例 1:
# 
# 输入: n = 3, k = 3
# 输出: "213"
# 
# 
# 示例 2:
# 
# 输入: n = 4, k = 9
# 输出: "2314"
# 
# 
#

# @lc code=start
class Solution:
    # 回溯法 https://leetcode-cn.com/problems/permutation-sequence/solution/jian-ji-cppdfsjian-zhi-by-edward_wang/
    def getPermutation(self, n: int, k: int) -> str:
        factorials, nums = [1], ['1']
        for i in range(1, n):
            # generate factorial system bases 0!, 1!, ..., (n - 1)!
            factorials.append(factorials[i - 1] * i)
            # generate nums 1, 2, ..., n
            nums.append(str(i + 1))
        print(factorials, nums)
        # fit k in the interval 0 ... (n! - 1)
        k -= 1
        # compute factorial representation of k
        output = []
        # https://pic.leetcode-cn.com/93effd21b842e31ddb3d9a05477dade2e92f79948805343ce7108a7759dedddd-Draft-1.jpg
        for i in range(n - 1, -1, -1):
            print(i, k, factorials,output)
            # 找到适合的分支idx，//求商，即当前层剪掉的分支数，所以在此分支找到第分支即可
            idx = k // factorials[i]
            print(idx)
            k -= idx * factorials[i]
            # 回溯法，可append(nums[idx])，其实是append第idx+1个数，索引值对应的就是idx
            output.append(nums[idx])
            # 回溯法，可从图https://pic.leetcode-cn.com/93effd21b842e31ddb3d9a05477dade2e92f79948805343ce7108a7759dedddd-Draft-1.jpg看到
            # 每个分支的当下都是del 了当前分支的数，，看图理解吧
            del nums[idx]
        
        return ''.join(output)






# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.getPermutation( n =4, k = 17))
