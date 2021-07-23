#
# @lc app=leetcode.cn id=930 lang=python3
#
# [930] 和相同的二元子数组
#

# @lc code=start
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        ans = l1 = l2 = s1 = s2 = 0
        for r in range(n):
            s1 += nums[r]
            s2 += nums[r]
            while l1 <= r and s1 > goal:
                s1 -= nums[l1]
                l1 += 1
            while l2 <= r and s2 >= goal:
                s2 -= nums[l2]
                l2 += 1
            ans += l2 - l1
        return ans

# @lc code=end

