#
# @lc app=leetcode.cn id=1572 lang=python3
#
# [1572] 矩阵对角线元素的和
#
# https://leetcode-cn.com/problems/matrix-diagonal-sum/description/
#
# algorithms
# Easy (80.50%)
# Likes:    30
# Dislikes: 0
# Total Accepted:    16.5K
# Total Submissions: 20.5K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给你一个正方形矩阵 mat，请你返回矩阵对角线元素的和。
# 
# 请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。
# 
# 
# 
# 示例  1：
# 
# 
# 
# 
# 输入：mat = [[1,2,3],
# [4,5,6],
# [7,8,9]]
# 输出：25
# 解释：对角线的和为：1 + 5 + 9 + 3 + 7 = 25
# 请注意，元素 mat[1][1] = 5 只会被计算一次。
# 
# 
# 示例  2：
# 
# 
# 输入：mat = [[1,1,1,1],
# [1,1,1,1],
# [1,1,1,1],
# [1,1,1,1]]
# 输出：8
# 
# 
# 示例 3：
# 
# 
# 输入：mat = [[5]]
# 输出：5
# 
# 
# 
# 
# 提示：
# 
# 
# n == mat.length == mat[i].length
# 1 <= n <= 100
# 1 <= mat[i][j] <= 100
# 
# 
#

# @lc code=start
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        l = len(mat)
        for i in range(l):
            if i != l - i - 1:
                res += mat[i][i] + mat[i][l - i - 1]
            else: res += mat[i][i]
        return res
# @lc code=end

