# Contains Dupilcate Problem:
# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

# Example 1:

# Input: [1,2,3,1]
# Output: true
# Example 2:

# Input: [1,2,3,4]
# Output: false
# Example 3:

# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true

class Solution(object):
    def containsDuplicate(
        self, nums: List[int]
    ) -> bool:
        return len(set(nums)) < len(nums)

# Success
# Details 
# Runtime: 176 ms, faster than 29.46% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 19.2 MB, less than 53.16% of Python3 online submissions for Contains Duplicate.


# Add Two Numbers Problem:
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        result_tail = result
        currentVal = 0
        
        while l1 or l2 or currentVal:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            currentVal, out = divmod(val1 + val2 + currentVal, 10)
        
            result_tail.next = ListNode(out)
            result_tail = result_tail.next                      
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
               
        return result.next

# Success
# Details 
# Runtime: 108 ms, faster than 24.71% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 13.8 MB, less than 83.50% of Python3 online submissions for Add Two Numbers.