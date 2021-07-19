#
# @lc app=leetcode.cn id=1310 lang=python3
#
# [1310] 子数组异或查询
#

# @lc code=start
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xor_arr = []
        res = []
        xor_arr.append(0)
        for i in range(len(arr)):
            xor_arr.append(xor_arr[-1] ^ arr[i])
        for query in queries:
            if query[0] != query[1]: 
                res.append(xor_arr[query[1] + 1] ^ xor_arr[query[0]])
            else:
                res.append(arr[query[0]])
        return res
# @lc code=end

