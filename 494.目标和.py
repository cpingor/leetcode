#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sums = sum(nums)
        if sums < target:
            return 0
        target += sums
        if target % 2 == 1:
            return 0
        target //= 2
        dp = [1] + [0] * target
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[target]
# @lc code=end

