#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0
        def backtracking(qs, count, remove):
            nonlocal ans
            if count == n:
                ans += 1
            else:
                if len(remove) == n:
                    return 
                remove = set()
                for i, j in qs:
                    remove.add(j)
                    if j + abs(count - i) < n:
                        remove.add(j + abs(count - i))
                    if j - abs(count - i) > -1:
                        remove.add(j - abs(count - i))
                for j in range(n):
                    if j in remove:
                        continue
                    backtracking(qs + [(count, j)], count + 1, remove)
        backtracking([], 0, set())
        return ans
# @lc code=end

