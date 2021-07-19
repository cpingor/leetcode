#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        if sum(candidates) < target:
            return []
        candidates.sort()
        def backtrack(chosen, candidate):
            if sum(chosen) == target:
                ans.add(tuple(chosen))
                return 

            if sum(chosen) > target:
                return

            for i, v in enumerate(candidate):
                if i > 0 and candidate[i - 1] == candidate[i]:
                    continue
                backtrack(chosen + [v], candidate[i + 1:])
            
        backtrack([], candidates)
        return list(map(list, ans))
# @lc code=end

