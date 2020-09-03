#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#
# https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (30.08%)
# Likes:    330
# Dislikes: 0
# Total Accepted:    43.1K
# Total Submissions: 136.1K
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# 给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
#
# 注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
#
#
#
# 示例 1：
#
# 输入：
# ⁠ s = "barfoothefoobarman",
# ⁠ words = ["foo","bar"]
# 输出：[0,9]
# 解释：
# 从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
# 输出的顺序不重要, [9,0] 也是有效答案。
#
#
# 示例 2：
#
# 输入：
# ⁠ s = "wordgoodgoodgoodbestword",
# ⁠ words = ["word","good","best","word"]
# 输出：[]
#
#
#
import copy
from itertools import permutations
from typing import *
# @lc code=start


class Solution:
    def __init__(self):
        self.res = []

    def brute_force(self, s: str, words: List[str]) -> List[int]:
        all_words = [''.join(_) for _ in permutations(words)]
        word_len, words_count = len(words[0]), len(words)
        window = words_count*word_len
        if window == len(s) and s in all_words:
            return [0]
        _, roads = 0, len(s[:-window+1])
        # 窗口为words_count*word_len的尺寸进行滑动
        while _ < roads:
            cur_window = s[_:_+window]
            if cur_window in all_words:
                self.res.append(_)
            __, _roads = 1, window-word_len+1
            if words_count == 1:
                _ += 1
                continue
            # 窗口为word_len的尺寸进行滑动
            while __ < _roads:
                cur_word = cur_window[__:__+word_len]
                if cur_word in words:
                    break
                __ += 1
            _ += __
        return self.res

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        # if not s or not words:
        #     return []
        word_len, words_count = len(words[0]), len(words)
        words_dict = {_:words.count(_) for _ in set(words)}
        # from collections import Counter
        # words_dict =  Counter(words)
        window = words_count*word_len
        # if len(s) < window:
        #     return []
        # if window == len(s) and s in all_words:return [0]
        def window_slide(words_dict, L):
            count,R = 0,L
            worddic_copy = words_dict.copy()
            while count < words_count:
                curslide = s[R:R+word_len]
                if worddic_copy.get(curslide, 0) == 0:break
                R += word_len
                worddic_copy[curslide] -= 1
                count += 1
            return count

        res = [L for L in range(len(s)-window+1) if window_slide(words_dict, L) == words_count]
        return res

# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.findSubstring("abcabac", ["ab", "ac"]))
