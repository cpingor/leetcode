#
# @lc app=leetcode.cn id=1235 lang=python3
#
# [1235] 规划兼职工作
#

# @lc code=start
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        m = max(endTime) + 1
        temp = []
        for i in range(len(profit)):
            temp.append((startTime[i], endTime[i], profit[i]))
        temp.sort()
        dp = [0] * m
        for i in range(len(endTime)):
            k = 0
            for j in range(i + 1):
                if temp[j][1] <= temp[i][0] and dp[k] <= dp[temp[j][1]]:
                    k = temp[j][1]
            dp[temp[i][1]] = max(dp[temp[i][1]], dp[k] + temp[i][2])
        return max(dp)

# @lc code=end

