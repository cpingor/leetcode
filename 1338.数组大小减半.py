#
# @lc app=leetcode.cn id=1338 lang=python3
#
# [1338] 数组大小减半
#

# @lc code=start
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = {}
        for i in arr:
            count[i] = count.get(i, 0) + 1
        sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        n = len(arr)
        ans = 0
        sums = 0
        for _, num in sorted_count:
            sums += num
            ans += 1
            if sums >= n // 2:
                return ans

# @lc code=end

