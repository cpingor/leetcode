#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        vis = [0] * l
        self.res = []
        self.back([], nums, vis)
        return self.res
    
    def back(self, s, nums, vis):
        if len(s) == len(nums):
            self.res.append(s)
            return
        for i in range(len(nums)):
            if vis[i] == 1:
                continue
            if i > 0 and nums[i - 1] == nums[i] and vis[i - 1] == 0:
                continue
            vis[i] = 1
            self.back(s + [nums[i]], nums, vis)
            vis[i] = 0
        

# @lc code=end

