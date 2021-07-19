#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []
        counts = {}
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 0
        for i, v in counts.items():
            heapq.heappush(h, (v, i))
            if len(h) > k:
                heapq.heappop(h)
        ans = []
        for item in h:
            ans.append(item[1])
        return ans  

# @lc code=end

