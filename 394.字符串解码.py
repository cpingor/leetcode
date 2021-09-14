#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
            else:
                tmp = ""
                while stack[-1] != "[":
                    tmp = stack.pop(-1) + tmp
                stack.pop(-1)
                times = ""
                while stack and stack[-1].isdigit():
                    times = stack.pop(-1) + times
                times = int(times)
                
                tmp = tmp * times
                for t in tmp:
                    stack.append(t)
        return "".join(stack)


# @lc code=end

