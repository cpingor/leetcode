#
# @lc app=leetcode.cn id=1234 lang=python3
#
# [1234] 替换子串得到平衡字符串
#

# @lc code=start
class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s) // 4
        ans = len(s)
        target = {}
        count = 0
        dic = {}
        l = 0
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        for i in dic:
            if dic[i] > n:
                target[i] = dic[i] - n
                count += dic[i] - n
        if count == 0:
            return 0
        for r in range(len(s)):
            if s[r] in target:
                if target[s[r]] > 0:
                    count -= 1
                target[s[r]] -= 1
                if count == 0:
                    while True:
                        c = s[l]
                        l += 1
                        if c in target:
                            target[c] += 1
                            if target[c] == 1:
                                count += 1
                                break
                    ans = min(ans, r - l + 2)            
        return ans
# @lc code=end

