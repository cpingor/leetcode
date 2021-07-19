#
# @lc app=leetcode.cn id=1497 lang=python3
#
# [1497] 检查数组对是否可以被 k 整除
#

# @lc code=start
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mod_list = [0] * k
        for x in arr:
            mod_list[x % k] += 1
        return mod_list[1:] == list(reversed(mod_list[1:])) and not mod_list[0] % 2
# @lc code=end


