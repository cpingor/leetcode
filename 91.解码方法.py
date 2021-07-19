#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        # s.lstrip('0')
        n = len(s)
        dp = [1] + [0] * n
        for i in range(n):
            if 0 < int(s[i]) < 10:
                dp[i + 1] += dp[i]
            if i > 0 and 9 < int(s[i - 1: i + 1]) < 27:
                dp[i + 1] += dp[i - 1]
        return dp[-1]
        # ans = 0
        # def dfs(s):
        #     nonlocal ans
        #     if len(s) == 0:
        #         ans += 1
        #     else:
        #         if s[0] == '0':
        #             return 
        #         else:
        #             dfs(s[1:])
        #             if 9 < int(s[:2]) < 27:
        #                 dfs(s[2:])
        # dfs(s)
        # return ans
# @lc code=end

