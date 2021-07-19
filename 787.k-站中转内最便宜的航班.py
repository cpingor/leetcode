#
# @lc app=leetcode.cn id=787 lang=python3
#
# [787] K 站中转内最便宜的航班
#

# @lc code=start
import heapq
import collections
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for fr, to, price in flights:
            graph[fr].append((to, price))
        return self.dijkstra(graph, src, dst, k + 1)

    def dijkstra(self, graph, start, end, k):
        heap = [(0, start, 0)]
        visited = set()
        while heap:
            (cost, u, steps) = heapq.heappop(heap)
            if (u, steps) in visited:
                continue
            visited.add((u, steps))
            if steps > k:continue
            if u == end:
                return cost
            for v, c in graph[u]:
                if (v, steps) is visited:
                    continue
                next = cost + c
                heapq.heappush(heap, (next, v, steps + 1))
        return -1

        
# @lc code=end

