#
# @lc app=leetcode.cn id=857 lang=python3
#
# [857] 雇佣 K 名工人的最低成本
#

# @lc code=start
import heapq
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        values = [(q / w, q) for q, w in zip(quality, wage)]
        ans = float('inf')
        values.sort(key=lambda a:-a[0])
        h = []
        total = 0
        for eff, q in values:
            heapq.heappush(h, -q)
            total += q
            print(total, ans, eff)
            if len(h) > k:
                total += heapq.heappop(h)
            if len(h) == k:
                ans = min(ans, total / eff)
        return ans

# @lc code=end

