#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#
# https://leetcode-cn.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (46.32%)
# Likes:    230
# Dislikes: 0
# Total Accepted:    35.5K
# Total Submissions: 76.5K
# Testcase Example:  '"25525511135"'
#
# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
# 
# 示例:
# 
# 输入: "25525511135"
# 输出: ["255.255.11.135", "255.255.111.35"]
# 
#

# @lc code=start
from typing import List
class Solution:
    def __init__(self):
        self.rec = []
        self.flag = 0
    """回溯加剪枝"""
    def traceback(self, num:int, tmp:str, s:str):
        if num==4 and not s:
            self.rec.append(tmp[:-1])
            return
        elif num >4:
            return
        for i in range(1,4):
            # 讲ip字符串隔成四部分i<=len(s)
            # 每个部分的数值必须小于255也就是2**8-1也就是(1<<8)-1
            # 若某个部分的第一位字符为'0'则此部分字符必为'0'，也就是说不能出现'012','01'这种情况
            if i<=len(s) and int(s[:i])<=(1<<8)-1 and (s[0]!='0' or s[:i]=='0'):
                print(tmp+s[:i]+'.')
                self.flag += 1
                # if self.flag != 4:
                self.traceback(num+1,tmp+s[:i]+'.', s[i:] if i<len(s) else "")

    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s)<=12:
            self.traceback(0, "", s)
        else:
            return []
        
        return self.rec
            
# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.restoreIpAddresses("25525511135"))
