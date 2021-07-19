#
# @lc app=leetcode.cn id=987 lang=python3
#
# [987] 二叉树的垂序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from operator import itemgetter
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.res = {}
        def bfs(root, i, j):
            if root is None:
                return 
            self.res.setdefault(j, []).append((i, root.val))
            bfs(root.left, i + 1, j - 1)
            bfs(root.right, i + 1, j + 1)
        bfs(root, 0, 0)
        return [list(map(itemgetter(1), sorted(self.res[k]))) for k in sorted(self.res)] 

# @lc code=end

