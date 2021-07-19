#
# @lc app=leetcode.cn id=837 lang=python3
#
# [837] 新21点
#

# @lc code=start
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0 if x > n else 1 for x in range(k + maxPts)]
        s = sum(dp[k:])
        for i in range(k - 1, -1, -1):
            dp[i] = s / maxPts
            s = s - dp[i + maxPts] + dp[i]
        return dp[0]

# @lc code=end

