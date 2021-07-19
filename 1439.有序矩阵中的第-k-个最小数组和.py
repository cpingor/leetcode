#
# @lc app=leetcode.cn id=1439 lang=python3
#
# [1439] 有序矩阵中的第 k 个最小数组和
#

# @lc code=start
import heapq
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        h = []
        cur = ([0] * len(mat))
        seen = set(cur)
        heapq.heappush(h, (sum(x[0] for x in mat), cur))
        count = 0
        while count < k:
            val, pointer = heapq.heappop(h)
            for i, ind in enumerate(pointer):
                temp = list(pointer)
                if ind + 1 < len(mat[0]):
                    temp[i] += 1
                else:
                    continue
                tt = tuple(temp)
                if tt not in seen:
                    heapq.heappush(h, (val - mat[i][ind] + mat[i][ind + 1], tt))
                    seen.add(tt)
            count += 1
        return val
        
# @lc code=end

