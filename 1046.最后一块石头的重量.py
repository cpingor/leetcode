#
# @lc app=leetcode.cn id=1046 lang=python3
#
# [1046] 最后一块石头的重量
#

# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            a = stones.pop()
            b = stones.pop()
            stones.append(a - b)
            if len(stones) == 1:
                return stones[0]
        return stones[0]
# @lc code=end

