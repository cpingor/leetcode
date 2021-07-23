#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l = r = 0
        while r < len(s):
            if s[r] not in s[l : r]:
                r += 1
            else:
                l += 1
            if r - l > ans:
                ans = r - l
        return ans
        
            
# @lc code=end

