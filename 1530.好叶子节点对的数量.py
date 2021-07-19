#
# @lc app=leetcode.cn id=1530 lang=python3
#
# [1530] 好叶子节点对的数量
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(root, path):
            if root.left:
                dfs(root.left, path + 1)
            if root.right:
                dfs(root.right, path + 1)
            if not root.left and not root.right:
                dic[root] = path
        stack = deque([root])
        visited = set()
        while stack:
            dic = {}
            root = stack.popleft()
            dfs(root, 0)
            temp = list(dic.items())
            for i in range(len(dic) - 1):
                for j in range(i + 1, len(dic)):
                    if temp[i][1] + temp[j][1] <= distance:
                        visited.add((temp[i][0], temp[j][0]))
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return len(visited)
# @lc code=end

