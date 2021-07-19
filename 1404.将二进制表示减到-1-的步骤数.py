#
# @lc app=leetcode.cn id=1404 lang=python3
#
# [1404] 将二进制表示减到 1 的步骤数
#

# @lc code=start
class Solution:
    def bi_add(self, s):
        flag = 1
        s_list = list(s)
        for i in range(len(s) - 1, -1, -1):
            if s_list[i] == '0':
                s_list[i] = '1'
                flag = 0
                break
            else:
                s_list[i] = '0'
        if flag:
            return '1' + ''.join(s_list)
        return ''.join(s_list)


    def numSteps(self, s: str) -> int:
        i = 0
        while s != '1':
            if int(s[-1]) % 2 == 1:
                s = self.bi_add(s)
            else:
                s = s[:-1]
            i += 1
        return i
# @lc code=end

