#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#
from functools import cmp_to_key
# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s_nums = list(map(str, nums))
        s_nums.sort(key=cmp_to_key(lambda x, y: 1 if x + y < y + x else -1))
        return ''.join(s_nums)[:-1].lstrip('0') + ''.join(s_nums)[-1]
# @lc code=end

