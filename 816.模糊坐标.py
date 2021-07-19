#
# @lc app=leetcode.cn id=816 lang=python3
#
# [816] 模糊坐标
#

# @lc code=start
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s[1:-1]
        ans = []
        xPoss = []
        def process(st, j):
            if j:
                for x in xPoss:
                    ans.append("(" + x + ', ' + st + ')')
            else:
                xPoss.append(st)
        for i in range(1, len(s)):
            strs = [s[:i], s[i:]]
            xPoss = []
            for j in range(2):
                if xPoss or not j:
                    st = strs[j]
                    if len(st) == 1 or st[0] != "0":
                        process(st, j)
                    if len(st) > 1 and st[-1] != '0':
                        process(st[:1] + '.' + st[1:], j)
                    if len(st) > 2 and st[0] != '0' and st[-1] != '0':
                        for k in range(2, len(st)):
                            process(st[:k] + '.' + st[k:], j)
        return ans


# @lc code=end

