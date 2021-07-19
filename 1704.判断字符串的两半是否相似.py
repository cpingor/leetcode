#
# @lc app=leetcode.cn id=1704 lang=python3
#
# [1704] 判断字符串的两半是否相似
#

# @lc code=start
from collections import Counter as counter
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l = len(s) // 2
        a = s[: l].lower()
        b = s[l :].lower()
        c = counter(a)
        d = counter(b)
        e, f = 0, 0
        for i in 'aeiou':
            e += c[i]
            f += d[i]
        return e == f
        

# @lc code=end

