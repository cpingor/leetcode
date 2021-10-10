#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def backtracking(lists):
            if sum(lists) == n and len(lists) == k:
                ans.append(lists)
                return
            if sum(lists) > n or len(lists) > k:
                return 
            else:
                if lists:
                    t = lists[-1]
                else:
                    t = 1
                for i in range(t, 10):
                    if i not in lists:
                        backtracking(lists + [i])
        backtracking([])
        return ans

# @lc code=end

