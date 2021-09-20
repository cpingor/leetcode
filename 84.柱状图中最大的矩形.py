#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        h_t = heights[::-1]
        h_t.append(0)
        heights.append(0)
        stack = []
        index = [0] * len(heights)
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                top = stack.pop()
                index[top] = i - top
            stack.append(i)
        stack_r = []
        index_r = [0] * len(h_t)
        for i in range(len(h_t)):
            while stack_r and h_t[i] < h_t[stack_r[-1]]:
                top = stack_r.pop()
                index_r[top] = i - top
            stack_r.append(i)
        ans = 0
        for i in range(len(heights)):
            ans = max(ans, heights[i] * index[i] + h_t[n - i - 1] * index_r[n - i - 1] - heights[i])
        return ans
# @lc code=end

