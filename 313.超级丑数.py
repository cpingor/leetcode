#
# @lc app=leetcode.cn id=313 lang=python3
#
# [313] 超级丑数
#

# @lc code=start
import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ans = [1]
        visited = [1]
        count = 1
        for i in primes:
            heapq.heappush(ans, i)
        x = 1
        while count < n:
            x = heapq.heappop(ans)
            if x != visited[-1]:
                visited.append(x)
            else:
                continue
            for i in primes:
                heapq.heappush(ans, x * i)
            count += 1
        return x

# @lc code=end

