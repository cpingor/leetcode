#
# @lc app=leetcode.cn id=1622 lang=python3
#
# [1622] 奇妙序列
#

# @lc code=start

class Fancy:

    def __init__(self):
        self.fancy = []


    def append(self, val: int) -> None:
        self.fancy.append(val)


    def addAll(self, inc: int) -> None:
        for i in range(len(self.fancy)):
            self.fancy[i] += inc


    def multAll(self, m: int) -> None:
        for i in range(len(self.fancy)):
            self.fancy[i] *= m

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.fancy): return
        s, old_s = 0, 1
        t, old_t = 1, 0
        r, old_r = 1000000007, self.fancy[idx]
        while r != 0:
            quotient = old_r // r
            old_r, r = r, old_r - quotient * r
            old_s, s = s, old_s - quotient * s
            old_t, t = t, old_t - quotient * t
        x = old_s
        if x < 0:
            x += 1000000007
        return x

    



# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
# @lc code=end

