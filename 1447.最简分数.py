#
# @lc app=leetcode.cn id=1447 lang=python3
#
# [1447] 最简分数
#

# @lc code=start
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def is_simple(m, n):
            for i in range(2, m + 1):
                if m % i == 0 and n % i == 0:
                    return False
            return True
        if n == 1:
            return []
        res = []
        for i in range(1, n + 1):
            for j in range(1, i):
                if is_simple(j, i):
                    res.append('{}/{}'.format(j, i))
                else:
                    continue
        return res

# @lc code=end

