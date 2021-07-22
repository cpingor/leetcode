#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:            
        # need = {}
        # for i in t:
        #     need[i] = need.get(i, 0) + 1
        # ans_dict = {}
        # result = ''
        # ans = ''
        # min_ans = len(s) + 1
        # l = r = 0
        # while r < len(s):
        #     if s[r] not in t:
        #         r += 1
        #         l += 1
        #     else:
        #         break
        # while r < len(s):
        #     if s[r] in t:
        #         ans = s[l : r + 1]
        #         ans_dict[s[r]] = ans_dict.get(s[r], 0) + 1
        #         flag = True
        #         for i in need:
        #             if i not in ans_dict or ans_dict[i] < need[i]:
        #                 flag = False
        #         if flag and len(t) <= len(ans):
        #             if len(ans) < min_ans:
        #                 result = ans
        #                 min_ans = len(ans)
        #             ans_dict[s[l]] = ans_dict.get(s[l], 0) - 1
        #             l += 1
        #             ans_dict[s[r]] = ans_dict.get(s[r], 0) - 1
        #         else:
        #             r += 1
        #     else:
        #         r += 1
        # return result   
        # need = collections.defaultdict(int)
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        count = len(t)
        left = 0
        result = (0, float('inf'))
        for right, c in enumerate(s):          
            if c in need:
                if need[c] > 0:
                    count -= 1
                need[c] -= 1
                if count == 0:
                    while True:
                        c = s[left]
                        left += 1
                        if c in need:
                            need[c] += 1
                            if need[c] == 1:
                                count += 1
                                break
                    if right - left + 1 < result[1] - result[0]:
                        result = (left - 1, right)
        return '' if result[1] > len(s) else s[result[0]:result[1]+1]    
# @lc code=end

