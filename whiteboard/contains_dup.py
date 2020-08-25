# Contains Dupilcate Problem:
# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

# Example 1:
Input: [1,2,3,1]
Output: true

# Example 2:
Input: [1,2,3,4]
Output: false

# Example 3:
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

class Solution(object):
    def containsDuplicate(self, nums: List[int]) -> bool:
        # length of set numbers less than numbers
        return len(set(nums)) < len(nums)
        print(nums)

# Success
# Details 
# Runtime: 176 ms, faster than 29.46% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 19.2 MB, less than 53.16% of Python3 online submissions for Contains Duplicate.

