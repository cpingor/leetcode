#
# @lc app=leetcode.cn id=1155 lang=python3
#
# [1155] 掷骰子的N种方法
#

# @lc code=start
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0] * (target + 1) for _ in range(d + 1)]
        dp[0][0] = 1
        for i in range(1, d + 1):
            for j in range(1, target + 1):
                for k in range(1, min(j, f) + 1):
                    dp[i][j] += dp[i - 1][j - k]
        return dp[d][target] % (10 ** 9 + 7)
# @lc code=end
