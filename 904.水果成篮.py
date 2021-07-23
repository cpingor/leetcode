#
# @lc app=leetcode.cn id=904 lang=python3
#
# [904] 水果成篮
#

# @lc code=start
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = 0
        cur = []
        l = r = 0
        for fruit in fruits:
            if fruit not in cur:
                if len(set(cur)) < 2:
                    cur.append(fruit)
                else:
                    ans = max(ans, r - l)
                    c = cur[-1]
                    for i in range(len(cur) - 1, -1, -1):
                        if cur[i] != c:
                            cur = cur[i + 1:]
                            r = len(cur)
                            l = 0
                            break
                    cur.append(fruit)
            else:
                cur.append(fruit)
            r += 1
        return max(ans, r - l)
                



# @lc code=end

