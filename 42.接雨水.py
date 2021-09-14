#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # if not height:
        #     return 0

        # n = len(height)
        # left_max = [height[0]] + [0] * (n - 1)
        # for i in range(1, n):
        #     left_max[i] = max(left_max[i - 1], height[i])

        # right_max = [0] * (n - 1) + [height[n - 1]]
        # for i in range(n - 2, -1, -1):
        #     right_max[i] = max(right_max[i + 1], height[i])
        # ans = sum(min(left_max[i], right_max[i]) - height[i] for i in range(n))
        # return ans       

        # ans = 0
        # stack = []
        # n = len(height)

        # for i, h in enumerate(height):
        #     while stack and h > height[stack[-1]]:
        #         peek = stack.pop()
        #         if not stack:
        #             break
        #         left = stack[-1]
        #         curr_width = i - left - 1
        #         curr_height = min(height[left], h) - height[peek]
        #         ans += curr_height * curr_width
        #     stack.append(i)
        
        # return ans
        ans = 0
        left_max, right_max = 0, 0
        left = 0
        right = len(height) - 1
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max < height[right]:
                ans += left_max - height[left]
                left += 1
            else:
                ans += right_max - height[right]
                right -= 1
        return ans



# @lc code=end