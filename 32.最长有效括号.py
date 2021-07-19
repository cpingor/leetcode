#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = len(s)
        if l == 0:
            return 0
        dp = [0] * l # dp[i] represents the count before index i
        for i in range(1, l):
            if s[i] == ')':
                pre = i - dp[i - 1] - 1
                if pre >= 0 and s[pre] == '(':
                    dp[i] = dp[i - 1] + 2
                    if pre > 0:
                        dp[i] += dp[pre - 1]
        return max(dp)



# @lc code=end

