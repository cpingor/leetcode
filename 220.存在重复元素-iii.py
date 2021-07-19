# @before-stub-for-debug-begin
from python3problem220 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=220 lang=python3
#
# [220] 存在重复元素 III
#

# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        n = len(nums)
        s = {}
        w = t + 1
        for i in range(n):
            x = nums[i]
            id = x // w
            if id in s:
                return True
            if id - 1 in s and abs(x - s[id - 1]) <= t:
                return True
            if id + 1 in s and abs(x - s[id + 1]) <= t:
                return True
            s[id] = x
            if i >= k:
                s.pop(nums[i - k] // w)
        return False


# @lc code=end

