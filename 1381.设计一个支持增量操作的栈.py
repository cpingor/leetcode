#
# @lc app=leetcode.cn id=1381 lang=python3
#
# [1381] 设计一个支持增量操作的栈
#

# @lc code=start
class CustomStack:

    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.stack = []


    def push(self, x: int) -> None:
        if len(self.stack) < self.max_size:
            self.stack.append(x)


    def pop(self) -> int:
        if len(self.stack):
            return self.stack.pop()
        else:
            return -1


    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
# @lc code=end

