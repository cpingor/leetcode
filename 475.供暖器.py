#
# @lc app=leetcode.cn id=475 lang=python3
#
# [475] 供暖器
#

# @lc code=start
from bisect import bisect_right
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        def possible(diameter):
            start = houses[0]
            l = 0
            for i in range(len(heaters)):
                if start < heaters[i] - diameter / 2:
                    return False
                end = heaters[i] + diameter / 2
                # idx = bisect_right(houses, end)
                # if idx >= len(houses):
                #     return True
                # start = houses[idx]
                r = len(houses) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if end < houses[mid]:
                        r = mid - 1
                    else:
                        l = mid + 1
                if l >= len(houses):
                    return True
                start = houses[l]
            return False


        l, r = 0, max(abs(houses[-1] - heaters[0]), abs(heaters[0] - houses[0])) * 2
        while l <= r:
            mid = (l + r) // 2
            if possible(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l // 2

# @lc code=end

