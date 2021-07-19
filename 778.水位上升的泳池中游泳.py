#
# @lc app=leetcode.cn id=778 lang=python3
#
# [778] 水位上升的泳池中游泳
#

# @lc code=start
from collections import deque
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def possible(t):
            if grid[0][0] > t:
                return False
            visited = set()
            side = len(grid)
            q = deque([(0, 0)])
            while q:
                i, j = q.popleft()
                if (i, j) in visited:
                    continue
                if i == side - 1 and j == side - 1:
                    return True
                visited.add((i, j))
                if i - 1 >= 0 and grid[i - 1][j] <= t and (i - 1, j) not in visited:
                    q.appendleft((i - 1, j))
                if j - 1 >= 0 and grid[i][j - 1] <= t and (i, j - 1) not in visited:
                    q.appendleft((i, j - 1))
                if i + 1 < side and grid[i + 1][j] <= t and (i + 1, j) not in visited:
                    q.appendleft((i + 1, j))
                if j + 1 < side and grid[i][j + 1] <= t and (i, j + 1) not in visited:
                    q.appendleft((i, j + 1))
            return False
        
        side = len(grid)
        l, r = grid[side - 1][side - 1], max(map(max, grid))
        while l <= r:
            mid = (l + r) // 2
            if possible(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
# @lc code=end

