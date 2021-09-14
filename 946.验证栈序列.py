#
# @lc app=leetcode.cn id=946 lang=python3
#
# [946] 验证栈序列
#

# @lc code=start
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        for i in pushed:
            stack.append(i)
            while stack and popped and popped[0] == stack[-1]:
                stack.pop()
                popped.pop(0)
            if len(popped) == 0:
                return True
        if popped:
            return False
# @lc code=end

