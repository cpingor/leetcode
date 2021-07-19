#
# @lc app=leetcode.cn id=875 lang=python3
#
# [875] 爱吃香蕉的珂珂
#

# @lc code=start
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            mid = (l + r) // 2
            if mid == 0:
                return 1
            temp = 0
            for i in piles:
                temp += math.ceil(i / mid)
            if temp > h:
                l = mid + 1
            else:
                r = mid - 1 
        return l

# @lc code=end

