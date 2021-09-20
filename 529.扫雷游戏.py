#
# @lc app=leetcode.cn id=529 lang=python3
#
# [529] 扫雷游戏
#

# @lc code=start
class Solution:
    def neighbor(self, board, click):
        x, y = click
        count = 0
        for i in range(max(0, x-1), min(x + 2, len(board))):
            for j in range(max(0, y-1), min(y + 2, len(board[0]))):
                if board[i][j] == 'M':
                    count += 1
        return count

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        elif board[x][y] == 'E':
            if self.neighbor(board, (x, y)) == 0:
                board[x][y] = 'B'
                for i in range(max(0, x-1), min(x + 2, len(board))):
                    for j in range(max(0, y-1), min(y + 2, len(board[0]))):
                        if board[i][j] != 'M':
                            self.updateBoard(board, [i, j])
            else:
                board[x][y] = str(self.neighbor(board, (x, y)))
            return board
        else:
            return board
            
# @lc code=end

