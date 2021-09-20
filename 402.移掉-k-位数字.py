#
# @lc app=leetcode.cn id=402 lang=python3
#
# [402] 移掉 K 位数字
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # 单调递增栈
        if len(num) <= k:
            return '0'
        stack = []
        for i in num:
            while k and stack and i < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(i)
        if k: stack = stack[:-k]
        ans = ''.join(stack).lstrip('0')
        return ans or '0'
        
# @lc code=end

