"""
【编码题】字符串S由小写字母构成，长度为n。定义一种操作，每次都可以挑选字符串中任意的两个相邻字母进行交换。询问在至多交换m次之后，字符串中最多有多少个连续的位置上的字母相同？



输入描述:
第一行为一个字符串S与一个非负整数m。(1 <= |S| <= 1000, 1 <= m <= 1000000)

输出描述:
一个非负整数，表示操作之后，连续最长的相同字母数量。

输入例子1:
abcbaa 2

输出例子1:
2

例子说明1:
使2个字母a连续出现，至少需要3次操作。即把第1个位置上的a移动到第4个位置。
所以在至多操作2次的情况下，最多只能使2个b或2个a连续出现。
"""


import copy
# s, m = tuple(input().split())
s, m = 'zoiumptccefmqdrjhhlgeyljbofwgvwogmvmpzgmoxdrbfdggimzifpfqmrqnrqrlobhluunzhyxrsicdhsrxpsrurqrewvrrcqc', 200
m = int(m)

# 拆分字符串成独立字符
s_list = [__ for __ in s]
# 构建字典 字符串：list(字符串的位置)
s_dict = {
    value: [k for k, v in enumerate(s_list) if v == value]
    for value in set(s_list)
}
# 按照可构成长度最长的字符串降序排序的字符list
_s_dict_keys = sorted(
    s_dict.keys(), key=lambda x: len(s_dict[x]), reverse=True)
# 遍历 按照可构成长度最长的字符串降序排序的字符list 若可在k步中走到一起，则break 打印结果
res = 0
for _ in _s_dict_keys:
    if res >= len(s_dict[_]):
        break
    cur = s_dict[_][len(s_dict[_])//2+(-1+len(s_dict[_]) % 2)]
    s_dict[_].remove(cur)
    max_length = 1
    step = 0
    for s in s_dict[_]:
        if step + abs(cur-s) > m:
            break
        step += abs(cur-s)
        max_length += 1
        res = max(res, max_length)

print(res)
