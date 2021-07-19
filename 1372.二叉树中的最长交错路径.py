#
# @lc app=leetcode.cn id=1372 lang=python3
#
# [1372] 二叉树中的最长交错路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collections import deque
# class Solution:
#     def longestZigZag(self, root: TreeNode) -> int:
#         dic = {}
#         ans = 0
#         cache = deque([root])
#         while cache:
#             temp = 0
#             root = cache.popleft()
#             stack = deque([[root, 1, 0], [root, -1, 0]])
#             while stack:
#                 node, dir, path_len = stack.popleft()
#                 temp = max(temp, path_len)
#                 if (node, dir) in dic:
#                     continue
#                 if dir == 1:
#                     if node.left:
#                         dic[(node, dir)] = temp
#                         dir *= -1
#                         stack.appendleft([node.left, dir, path_len + 1]) 
#                 else:
#                     if node.right:
#                         dic[(node, dir)] = temp
#                         dir *= -1
#                         stack.appendleft([node.right, dir, path_len + 1])             
#             ans = max(ans, temp)
#             if root.left:
#                 cache.append(root.left)
#             if root.right:
#                 cache.append(root.right)
#         return ans
from collections import deque
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        queue = deque()
        queue.append((root, 0, 0))
        res = 0

        while queue:
            node, left, right = queue.popleft()
            res = max(res, left, right)
            if node.left:
                queue.append((node.left, 0, left+1))
            if node.right:
                queue.append((node.right, right+1, 0))
        return res
# @lc code=end

