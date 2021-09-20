#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = {}
        stack = []
        for i in nums2:
            while stack and i > stack[-1]:
                top = stack.pop()
                ans[top] = i
            stack.append(i)
        res = []
        for i in nums1:
            if i in ans:
                res.append(ans[i])
            else:
                res.append(-1)
        return res
# @lc code=end

