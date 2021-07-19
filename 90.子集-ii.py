#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def backtracking(nums, cand):
            ans.append(nums)
            for i, v in enumerate(cand):
                if i > 0 and cand[i] == cand[i-1]:
                    continue
                backtracking(nums + [v], cand[i + 1:])
        backtracking([], nums)
        return ans
# @lc code=end

