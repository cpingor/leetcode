#
# @lc app=leetcode.cn id=877 lang=python3
#
# [877] 石子游戏
#

# @lc code=start
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # return True
        l = len(piles)
        dp = [0] * l
        for i, v in enumerate(piles):
            dp[i] = v
        for i in range(l - 2, -1, -1):
            for j in range(i + 1, l):
                dp[j] = max(piles[i] - dp[j], piles[j] - dp[j - 1])
        return dp[l - 1] > 0

# @lc code=end

