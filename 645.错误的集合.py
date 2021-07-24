#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ln, total = len(nums), sum(set(nums))
        return [sum(nums) - total, (1 + ln) * ln // 2 - total]

# @lc code=end

