#
# @lc app=leetcode.cn id=525 lang=python3
#
# [525] 连续数组
#

# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if sum(nums) * 2 == n:
            return n
        counter = {0 : -1}
        ans = 0
        count = 0
        for i, v in enumerate(nums):
            if v == 1:
                count += 1
            else:
                count -= 1
            if count in counter:
                ans = max(ans, i - counter[count])
            else:
                counter[count] = i
        return ans

# @lc code=end

