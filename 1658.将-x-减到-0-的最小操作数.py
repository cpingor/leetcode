#
# @lc app=leetcode.cn id=1658 lang=python3
#
# [1658] 将 x 减到 0 的最小操作数
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        ans = n + 1
        sum = 0
        for l1 in range(n):
            sum += nums[l1]
            if sum > x:
                sum -= nums[l1]
                l1 -= 1
                break
            if sum == x:
                ans = min(ans, l1 + 1)
        for r1 in range(n - 1, -1, -1):
            sum += nums[r1]
            while sum > x and l1 >= 0:
                sum -= nums[l1]
                l1 -= 1
            if sum == x:
                ans = min(ans, l1 + 1 + n - r1)
        return ans if ans != n + 1 else -1


# @lc code=end

