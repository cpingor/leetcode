#
# @lc app=leetcode.cn id=1738 lang=python3
#
# [1738] 找出第 K 大的异或坐标值
#

# @lc code=start
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        val = []
        res = []
        for a in range(m):
            res.append([])
            for b in range(n):
                if a == b == 0:
                    res[0].append(matrix[0][0])
                elif a == 0 and b > 0:
                    res[0].append(res[0][b - 1] ^ matrix[0][b])
                elif b == 0 and a != 0:
                    res[a].append(res[a - 1][0] ^ matrix[a][0])
                else:
                    res[a].append(res[a - 1][b - 1] ^ res[a][b - 1] ^ res[a - 1][b] ^ matrix[a][b])
        for x in res:
            val.extend(x)
        return sorted(val, reverse=True)[k - 1]
# @lc code=end

