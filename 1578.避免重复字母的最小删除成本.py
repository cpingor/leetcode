#
# @lc app=leetcode.cn id=1578 lang=python3
#
# [1578] 避免重复字母的最小删除成本
#

# @lc code=start
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        l = len(s)
        temp = s[0]
        res = 0
        k = 0
        for i in range(1, l):
            if s[i] == temp:
                if cost[i] > cost[k]:
                    res += cost[k]
                    k = i 
                else:
                    res += cost[i]
            else:
                k = i
                temp = s[i]
        return res
# @lc code=end

