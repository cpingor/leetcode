#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        ans = len(nums)
        total = 0
        if sum(nums) < target:
            return 0
        for j in range(len(nums)):
            total += nums[j]
            while total >= target:
                total -= nums[i]
                ans = min(ans, j - i + 1)
                i += 1
        return ans

# @lc code=end

