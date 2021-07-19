#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def backtrack(chosen, candidate):
            if sum(chosen) == target:
                ans.append(chosen)
                return 

            if sum(chosen) > target:
                return

            for i, v in enumerate(candidate):
                backtrack(chosen + [v], candidate[i:])
            
        backtrack([], candidates)
        return ans

            
# @lc code=end

