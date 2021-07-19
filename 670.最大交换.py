# @before-stub-for-debug-begin
from python3problem670 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=670 lang=python3
#
# [670] 最大交换
#

# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        s_num = str(num)
        for i, v in enumerate(s_num):
            m = max(s_num[i:])
            if m == v: continue
            r_m = s_num.rindex(m)

            l_num = list(s_num)
            l_num[i], l_num[r_m] = m, v
            return int(''.join(l_num))
        return num


# @lc code=end

