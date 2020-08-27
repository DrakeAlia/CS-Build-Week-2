# Given an integer array nums sorted in ascending order, and an integer target.

# Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You should search for target in nums and if you found return its index, otherwise return -1.

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1
 

# Constraints:

# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is guranteed to be rotated at some pivot.
# -10^4 <= target <= 10^4
# class Solution:
    # def search(self, nums: List[int], target: int) -> int:
def search(nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            middle = (l+r)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                if nums[r] < target and nums[middle] <= nums[r]:
                    r = middle - 1
                else:
                    l = middle + 1
            else:
                if target < nums[l] and nums[l] <= nums[middle]:
                    l = middle + 1
                else:
                    r = middle - 1
        return -1

# Runtime: 44 ms
# Memory Usage: 13.9 MB