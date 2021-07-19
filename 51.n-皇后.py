#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        def backtracking(grid, qs, count, remove):
            if count == n:
                ans.append(grid)
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
                    temp = ['.'] * n
                    temp[j] = 'Q'
                    backtracking(grid + [''.join(temp)], qs + [(count, j)], count + 1, remove)
        backtracking([], [], 0, set())
        return ans



# @lc code=end

