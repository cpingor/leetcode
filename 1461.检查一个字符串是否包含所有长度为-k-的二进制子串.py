#
# @lc app=leetcode.cn id=1461 lang=python3
#
# [1461] 检查一个字符串是否包含所有长度为 K 的二进制子串
#

# @lc code=start
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) <= k:
            return False
        set_k = set()
        index = 0
        while len(set_k) < 2 ** k and index <= len(s) - k:
            set_k.add(s[index : index + k])
            index += 1
        return len(set_k) == 2 ** k


# @lc code=end

