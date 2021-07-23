#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续1的个数 III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = 0
        # while r < len(nums): 
        #     if nums[r] == 0:
        #         k -= 1
        #     if k < 0:
        #         if nums[l] == 0:
        #             k += 1
        #         l += 1
        #     r += 1
        # return r - l
        res = 0
        suml = sumr = 0
        for r in range(len(nums)):
            sumr += 1 - nums[r]
            while suml < sumr - k:
                suml += 1 - nums[l]
                l += 1
            res = max(res, r - l + 1) 
        return res
# @lc code=end

