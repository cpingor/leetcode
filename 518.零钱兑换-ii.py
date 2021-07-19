#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for coin in coins:
            for i in range(1, amount + 1):
                if coin <= i:
                    dp[i] += dp[i - coin]
        return dp[-1]
# @lc code=end

