#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1].isalpha():
                    if i == 0:
                        dp[i][j] = False
                    elif p[j - 1] == s[i - 1]:
                        dp[i][j] |= dp[i - 1][j - 1]
                    else:
                        dp[i][j] = False
                elif p[j - 1] == '.':
                    dp[i][j] |= dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 2]
        return dp[-1][-1]
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         m, n = len(s), len(p)

#         def matches(i: int, j: int) -> bool:
#             if i == 0:
#                 return False
#             if p[j - 1] == '.':
#                 return True
#             return s[i - 1] == p[j - 1]

#         f = [[False] * (n + 1) for _ in range(m + 1)]
#         f[0][0] = True
#         for i in range(m + 1):
#             for j in range(1, n + 1):
#                 if p[j - 1] == '*':
#                     f[i][j] |= f[i][j - 2]
#                     if matches(i, j - 1):
#                         f[i][j] |= f[i - 1][j]
#                 else:
#                     if matches(i, j):
#                         f[i][j] |= f[i - 1][j - 1]
#         return f[m][n]
     

# @lc code=end

