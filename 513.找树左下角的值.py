# @before-stub-for-debug-begin
from python3problem513 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        bfs_node = [root]
        while bfs_node:
            layer_node = 0
            current_bfs_node = []
            for node in bfs_node:
                if node.left:
                    current_bfs_node.append(node.left)
                    layer_node += 1
                if node.right:
                    current_bfs_node.append(node.right)
                    layer_node += 1
            if layer_node != 0:
                bfs_node = current_bfs_node
            else:
                return bfs_node[0].val
        
        
# @lc code=end

