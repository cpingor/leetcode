#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#

# @lc code=start
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        l = len(mat)
        m = len(mat[0])
        if l * m != r * c:
            return mat
        temp = []
        for i in range(l):
            temp.extend(mat[i])
        res = [[] for _ in range(r)] 
        x = 0
        for i in range(r):
            for _ in range(c):
                res[i].append(temp[x])
                x += 1
        return res
# @lc code=end

