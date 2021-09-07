#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        n = len(s)
        mapping = dict(zip(('I', 'V', 'X', 'L', 'C', 'D', 'M'), (1,5, 10, 50, 100, 500, 1000)))
        minus = {'I': 'VX', 'X': 'LC', 'C': 'DM'}
        for i, v in enumerate(s):
            if v in 'IXC':
                if i + 1 < n and s[i + 1] in minus[v]:
                    ans -= mapping[v]
                else:
                    ans += mapping[v]
            else:
                ans += mapping[v]
        return ans

# @lc code=end

