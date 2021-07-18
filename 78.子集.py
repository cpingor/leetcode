#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtracking(nums, cand):
            ans.append(nums)
            for i, v in enumerate(cand):
                backtracking(nums + [v], cand[i + 1:])
        backtracking([], nums)
        return ans 
# @lc code=end

