#
# @lc app=leetcode.cn id=1311 lang=python3
#
# [1311] 获取你好友已观看的视频
#

# @lc code=start
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        stack = [id]
        target = [id]
        while level:
            hh = []
            for i in target:
                for temp in friends[i]:
                    if temp not in stack:
                        stack.append(temp)
                        hh.append(temp)
            target = hh.copy()
            level -= 1
        videos = {}
        for i in target:
            for c in watchedVideos[i]:
                videos[c] = videos.get(c, 0) + 1
        xx = sorted(videos.items(), key=lambda x: (x[1], x[0]))
        res = []
        for x in xx:
            res.append(x[0])
        return res
                
# @lc code=end

