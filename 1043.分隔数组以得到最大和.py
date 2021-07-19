#
# @lc app=leetcode.cn id=1043 lang=python3
#
# [1043] 分隔数组以得到最大和
#

# @lc code=start
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        l = len(arr)
        if l <= k:
            return max(arr) * l
        dp = [0] * l
        for i in range(k):
            dp[i] = max(arr[:i + 1]) * (i + 1)
        for i in range(k, l):
            maxnum = 0
            for j in range(i, i - k, -1):
                maxnum = max(maxnum, arr[j])
                dp[i] = max(dp[i], dp[j - 1] + maxnum * (i - j + 1))  
        return dp[-1]            

# @lc code=end

