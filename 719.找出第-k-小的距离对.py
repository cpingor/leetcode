#
# @lc app=leetcode.cn id=719 lang=python3
#
# [719] 找出第 k 小的距离对
#

# @lc code=start
import heapq
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        def possible(mid):
            slow = 0
            ans = 0
            for fast in range(len(nums)):
                while nums[fast] - nums[slow] > mid:
                    slow += 1
                ans += fast - slow
            return ans >= k
        
        l, r = 0, nums[-1] - nums[0]
        while l <= r:
            mid = (l + r) // 2
            if possible(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l 

        
# @lc code=end

