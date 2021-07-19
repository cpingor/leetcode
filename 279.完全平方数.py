#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        sq = int(n ** 0.5)
        nums = [num ** 2 for num in range(1, sq + 1)]
        dp = [0] + [10001] * n
        for i in nums:
            for j in range(i, n + 1):
                dp[j] = min(dp[j], dp[j - i] + 1)
        return dp[n]
# @lc code=end

