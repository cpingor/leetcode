#
# @lc app=leetcode.cn id=863 lang=python3
#
# [863] 二叉树中所有距离为 K 的结点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(root, par=None):
            if root:
                root.par = par
                dfs(root.left, root)
                dfs(root.right, root)
        dfs(root)
        queue = deque([(target, 0)])
        visited = {target}
        while queue:
            if queue[0][1] == k:
                return [node[0].val for node in queue]
            node, d = queue.popleft()
            for item in (node.left, node.right, node.par):
                if item and item not in visited:
                    visited.add(item)
                    queue.append((item, d + 1))
        return []        

# @lc code=end

