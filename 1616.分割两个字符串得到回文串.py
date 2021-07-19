#
# @lc app=leetcode.cn id=1616 lang=python3
#
# [1616] 分割两个字符串得到回文串
#

# @lc code=start
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        left = len(a) // 2 - 1
        left = min(self.is_palindrome(a, a, left), self.is_palindrome(b, b, left))
        left = min(self.is_palindrome(a, b, left), self.is_palindrome(b, a, left))
        return left == -1

    def is_palindrome(self, s_l, s_r, left):
        right = len(s_l) - 1 - left
        while left >= 0 and right < len(s_l):
            if s_l[left] != s_r[right]:
                break
            left -= 1
            right += 1
        return left

# @lc code=end

