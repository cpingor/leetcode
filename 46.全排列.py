#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def backtracking(nums, candadates):
            if len(nums) == n:
                ans.append(nums)
            else:
                for i, v in enumerate(candadates):
                    backtracking(nums + [v], candadates[:i] + candadates[i + 1:])
        backtracking([], nums)
        return ans
# @lc code=end

