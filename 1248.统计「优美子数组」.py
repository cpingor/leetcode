#
# @lc app=leetcode.cn id=1248 lang=python3
#
# [1248] 统计「优美子数组」
#

# @lc code=start
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atmost(s):
            sum = l = 0
            ans = 0
            for r, c in enumerate(nums):
                sum += c % 2
                while sum > s:
                    sum -= nums[l] % 2
                    l += 1
                ans += r - l
            return ans
        return atmost(k) - atmost(k - 1)

# @lc code=end

