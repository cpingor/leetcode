#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_dict = {}
        ans = []
        for i in p:
            p_dict[i] = p_dict.get(i, 0) + 1
        l = 0
        temp = p_dict.copy()
        for r in range(len(s)):
            if s[r] not in p_dict:
                l = r + 1
                temp = p_dict.copy()
            else:
                temp[s[r]] -= 1
                if temp[s[r]] < 0:
                    while s[l] != s[r]:
                        temp[s[l]] += 1
                        l += 1
                    temp[s[l]] += 1
                    l += 1
                    continue
                if r - l + 1 == len(p):
                    ans.append(l)
                    temp[s[l]] += 1
                    l += 1
        return ans
            

# @lc code=end

