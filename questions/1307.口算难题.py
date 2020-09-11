#
# @lc app=leetcode.cn id=1307 lang=python3
#
# [1307] 口算难题
#
# https://leetcode-cn.com/problems/verbal-arithmetic-puzzle/description/
#
# algorithms
# Hard (33.21%)
# Likes:    26
# Dislikes: 0
# Total Accepted:    974
# Total Submissions: 2.9K
# Testcase Example:  '["SEND","MORE"]\n"MONEY"'
#
# 给你一个方程，左边用 words 表示，右边用 result 表示。
# 
# 你需要根据以下规则检查方程是否可解：
# 
# 
# 每个字符都会被解码成一位数字（0 - 9）。
# 每对不同的字符必须映射到不同的数字。
# 每个 words[i] 和 result 都会被解码成一个没有前导零的数字。
# 左侧数字之和（words）等于右侧数字（result）。 
# 
# 
# 如果方程可解，返回 True，否则返回 False。
# 
# 
# 
# 示例 1：
# 
# 输入：words = ["SEND","MORE"], result = "MONEY"
# 输出：true
# 解释：映射 'S'-> 9, 'E'->5, 'N'->6, 'D'->7, 'M'->1, 'O'->0, 'R'->8, 'Y'->'2'
# 所以 "SEND" + "MORE" = "MONEY" ,  9567 + 1085 = 10652
# 
# 示例 2：
# 
# 输入：words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"
# 输出：true
# 解释：映射 'S'-> 6, 'I'->5, 'X'->0, 'E'->8, 'V'->7, 'N'->2, 'T'->1, 'W'->'3',
# 'Y'->4
# 所以 "SIX" + "SEVEN" + "SEVEN" = "TWENTY" ,  650 + 68782 + 68782 = 138214
# 
# 示例 3：
# 
# 输入：words = ["THIS","IS","TOO"], result = "FUNNY"
# 输出：true
# 
# 
# 示例 4：
# 
# 输入：words = ["LEET","CODE"], result = "POINT"
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= words.length <= 5
# 1 <= words[i].length, results.length <= 7
# words[i], result 只含有大写英文字母
# 表达式中使用的不同字符数最大为 10
# 
# 
#

# @lc code=start
class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        # 找最长字符串的长度
        max_len = 0
        for word in words:
            max_len = max(max_len, len(word))

        # 如果相加的字符串长度 大于 结果的长度
        if max_len > len(result): return False
        max_len = max(max_len, len(result))
        # 重塑words,把每个字符串拉长max_len,用"#" 补齐,
        constr_words = []
        for word in words:
            constr_words.append(word.rjust(max_len, "#"))
        # 结果同样也是
        result = result.rjust(max_len, "#")
        # 按位取出
        arr = []
        for x in zip(*constr_words, result):
            arr.append(x)
        # 取反(从低位开始
        arr = arr[::-1]
        # 每个arr元素长度
        l = len(arr[0])
        # 所有数字
        all_num = set(range(10))
        # 已经使用的数字
        used_num = set()
        # 记录每个字母代表数字
        lookup = {"#": 0}

        # pos 表示到arr索引, idx 表示 arr[pos]索引, carry进位
        def dfs(pos, idx, carry):
            # 递归出口
            if pos == len(arr):
                if carry == 0:
                    return True
                else:
                    return False
            # 求在pos位是否满足条件
            if idx == l:
                tmp = 0
                for t in arr[pos][:-1]:
                    tmp += lookup[t]
                tmp += carry
                a, b = divmod(tmp, 10)
                if b != lookup[arr[pos][-1]]: return False
                return dfs(pos + 1, 0, a)
            # 判断字符串是否在lookup
            if arr[pos][idx] in lookup:
                return dfs(pos, idx + 1, carry)
            else:
                # 枚举
                for num in all_num - used_num:
                    # 保证首位不能为0
                    if ((pos + 1 < len(arr) and arr[pos + 1][idx] == "#") or pos - 1 == len(arr)) and num == 0: continue
                    used_num.add(num)
                    lookup[arr[pos][idx]] = num
                    if dfs(pos, idx + 1, carry): return True
                    lookup.pop(arr[pos][idx])
                    used_num.remove(num)
            return False

        return dfs(0, 0, 0)

# @lc code=end

