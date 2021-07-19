#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # n = sum(nums)
        # l = len(nums)
        # if n % 2 == 1:
        #     return False
        # target = n // 2
        # dp = [0] * (target + 1)
        # dp[0] = True
        # for num in nums:
        #     for j in range(target, num - 1, -1):
        #         dp[j] = dp[j] | dp[j - num]
        # return dp[-1] == 1
        bitmap, sum_num = 1, 0
        for num in nums:
            bitmap |= bitmap << num
            sum_num += num
        if sum_num & 1 == 1:
            return False
        return (1 << sum_num // 2 ) & bitmap != 0
        
# @lc code=end

