#
# @lc app=leetcode.cn id=978 lang=python3
#
# [978] 最长湍流子数组
#

# @lc code=start
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        ans = 1
        l = 0
        for r in range(len(arr) - 1):
            if l == r:
                if arr[l] == arr[l + 1]:        
                    l += 1
                r += 1
            else:
                if arr[r - 1] < arr[r] and arr[r] > arr[r + 1]:
                    r += 1
                elif arr[r - 1] > arr[r] and arr[r] < arr[r + 1]:
                    r += 1
                else:
                    l = r
            ans = max(ans, r - l + 1)
            
        return ans

# @lc code=end

