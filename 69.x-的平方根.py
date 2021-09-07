#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while l <= r:
            mid = l + r >> 1
            if mid * mid > x:
                r = mid - 1
            elif mid * mid == x:
                return mid
            else:
                l = mid + 1
        return l - 1
# @lc code=end

