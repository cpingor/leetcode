#
# @lc app=leetcode.cn id=1488 lang=python3
#
# [1488] 避免洪水泛滥
#

# @lc code=start
import bisect
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [1] * len(rains)
        lake = {}
        sunny = []
        for i, v in enumerate(rains):
            if v > 0:
                ans[i] = -1
                if v not in lake:
                    lake[v] = i
                else:
                    if sunny:
                        j = bisect.bisect_left(sunny, lake[v])
                        if j == len(sunny):
                            return []
                        ans[sunny.pop(j)] = v
                    else:
                        return []
                    lake[v] = i
            else:
                sunny.append(i)
        return ans


# @lc code=end

