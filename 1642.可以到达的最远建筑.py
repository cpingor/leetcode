#
# @lc app=leetcode.cn id=1642 lang=python3
#
# [1642] 可以到达的最远建筑
#
import heapq
# @lc code=start
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        h = []
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i - 1]
            if diff < 0:
                continue
            if bricks < diff and ladders:
                ladders -= 1
                if h and -h[0] > diff:
                    bricks -= heapq.heappop(h)
                else:
                    continue
            bricks -= diff
            if bricks < 0:
                return i - 1
            heapq.heappush(h, -diff)
        return len(heights) - 1
# @lc code=end

