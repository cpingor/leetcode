# @before-stub-for-debug-begin
from python3problem401 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#

# @lc code=start
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        time = [(0,0)]
        hours = [1, 2, 4, 8]
        minutes = [1, 2, 4, 8, 16, 32]
        def backtrack(start, hours, minutes, time):
            temp = time[-1]
            if start == turnedOn:
                ans.append('{}:{:0>2d}'.format(temp[0], temp[1]))
                return
            for i in hours:
                temp = time[-1]
                temp = (temp[0] + i, temp[1])
                if temp[0] > 11:
                    return
                time.append(temp)
                x = hours.index(i)
                new_hour = hours[:x] + hours[x + 1:]
                backtrack(start + 1, new_hour, minutes, time)
                time.pop()
            for i in minutes:
                temp = time[-1]
                temp = (temp[0], temp[1] + i)
                if temp[1] > 59:
                    return 
                time.append(temp)
                x = minutes.index(i)
                new_minutes = minutes[:x] + minutes[x + 1:]
                backtrack(start + 1, hours, new_minutes, time)
                time.pop()
        backtrack(0, hours, minutes, time)
        return list(set(ans))
# @lc code=end

