#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        new_hair = Node(-10001)
        cur = new_hair
        nodes = []
        ori_nodes = []
        temp = head
        while temp:
            new_node = Node(temp.val)
            ori_nodes.append(temp)
            cur.next = new_node
            temp = temp.next
            cur = cur.next
            nodes.append(new_node)
        cur_random = new_hair.next
        while head:
            if head.random:
                cur_random.random = nodes[ori_nodes.index(head.random)]
            head = head.next
            cur_random = cur_random.next
        return new_hair.next

# @lc code=end

