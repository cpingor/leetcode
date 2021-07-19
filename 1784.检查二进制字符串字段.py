#
# @lc app=leetcode.cn id=1784 lang=python3
#
# [1784] 检查二进制字符串字段
#

# @lc code=start
import itertools
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return len(list(itertools.groupby(s))) < 3
# @lc code=end

