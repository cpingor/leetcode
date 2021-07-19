#
# @lc app=leetcode.cn id=1255 lang=python3
#
# [1255] 得分最高的单词集合
#

# @lc code=start
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        self.ans = 0
        letter_dict = {}
        for c in letters:
            letter_dict[c] = letter_dict.get(c, 0) + 1
        def backtracking(cur, start, letter_dict):
            self.ans = max(self.ans, cur)
            for i in range(start, len(words)):
                scores = 0
                temp = letter_dict.copy()
                for c in words[i]:
                    if c in temp and temp[c] > 0:
                        temp[c] -= 1
                        scores += score[ord(c) - 97]
                    else:
                        scores = 0
                        break
                if scores > 0:
                    backtracking(cur + scores, i + 1, temp)                
        backtracking(0, 0, letter_dict)
        return self.ans
# @lc code=end

