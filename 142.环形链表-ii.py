#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        dis_a, dis_b = 0, 0
        flag = 0
        while fast and fast.next:
            if flag == 1:
                dis_b += 1
            elif flag == 0:
                dis_a += 1
            else:
                break
            if slow.next == fast.next.next:
                flag += 1
            slow = slow.next
            fast = fast.next.next
        if dis_b == 0:
            return None
        cycle1, cycle2 = head, slow
        if dis_a > dis_b:
            while dis_a != dis_b:
                cycle1 = cycle1.next
                dis_a -= 1
        elif dis_a < dis_b:
            while dis_a != dis_b:
                cycle2 = cycle2.next
                dis_b -= 1
        while dis_a >= 0:
            if cycle1 == cycle2 and cycle1:
                return cycle1
            else:
                cycle1 = cycle1.next
                cycle2 = cycle2.next
                dis_a -= 1
        return None 
        
# @lc code=end

