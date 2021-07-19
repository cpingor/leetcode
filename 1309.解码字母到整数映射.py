#
# @lc app=leetcode.cn id=1309 lang=python3
#
# [1309] 解码字母到整数映射
#

# @lc code=start
class Solution:
    def freqAlphabets(self, s: str) -> str:
        l = len(s)
        i = l - 1
        res = ''
        while i > -1:
            if s[i] == '#':
                res += chr(96 + int(s[i-2:i]))
                i -= 3
            else:
                res += chr(96 + int(s[i]))
                i -= 1
        return res[::-1]
# @lc code=end

