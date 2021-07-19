#
# @lc app=leetcode.cn id=650 lang=python3
#
# [650] 只有两个键的键盘
#

# @lc code=start
class Solution:
    def minSteps(self, n: int) -> int:
        iter = 0
        for i in range(2, n + 1):
            while n % i == 0:
                n //= i
                iter += i
            if n == 1:
                break
        return iter
# @lc code=end

