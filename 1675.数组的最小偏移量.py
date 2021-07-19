#
# @lc app=leetcode.cn id=1675 lang=python3
#
# [1675] 数组的最小偏移量
#

# @lc code=start
import heapq
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        mat = []
        for i in nums:
            temp = [i]
            if i % 2 == 1:
                temp.append(i * 2)
            while i % 2 == 0:
                i //= 2
                temp.append(i)
            temp.sort()
            mat.append(temp)
        l, r = 0, 10 ** 9 + 1
        h = [(row[0], i, 0) for i, row in enumerate(mat)]
        heapq.heapify(h)
        max_v = max(row[0] for row in mat)
        while True:
            min_v, row, col = heapq.heappop(h)
            if max_v - min_v < r - l:
                l, r = min_v, max_v
            if col == len(mat[row]) - 1:
                return r - l
            max_v = max(max_v, mat[row][col + 1])
            heapq.heappush(h, (mat[row][col + 1], row, col + 1))
# @lc code=end

