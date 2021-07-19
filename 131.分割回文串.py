#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # ans = []
        # n = len(s)
        # def is_pal(s):
        #     return s == s[::-1]
        # def backtracking(cur, i):
        #     if i == n:
        #         ans.append(cur)
        #     else:
        #         temp = ''
        #         for x, y in enumerate(s[i:]):
        #             temp += y
        #             if is_pal(temp):
        #                 backtracking(cur + [temp], i + x + 1)
        # backtracking([], 0)
        # return ans
        dp = [[] for _ in range(len(s) + 1)]
        dp[-1] = [[]]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] == s[i:j][::-1]:
                    for each in dp[j]:
                        dp[i].append([s[i:j]] + each)
        return dp[0]
# @lc code=end

