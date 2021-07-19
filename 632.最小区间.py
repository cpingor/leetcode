#
# @lc app=leetcode.cn id=632 lang=python3
#
# [632] 最小区间
#

# @lc code=start
import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        l, r = -10 ** 5 - 1, 10 ** 5 + 1
        h = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(h)
        max_v = max(row[0] for row in nums)
        while True:
            min_v, row, col = heapq.heappop(h)
            if max_v - min_v < r - l:
                l, r = min_v, max_v
            if col == len(nums[row]) - 1:
                return [l, r]
            max_v = max(max_v, nums[row][col + 1])
            heapq.heappush(h, (nums[row][col + 1], row, col + 1))
# @lc code=end

