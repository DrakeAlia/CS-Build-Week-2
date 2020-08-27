# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# class Solution(object):
    # def twoSum(self, nums, target):
def twoSums(nums):
        dictionary = dict()
        pos = 0
        while pos < len(nums):
            print(nums)
            if (target - nums[pos]) not in dictionary:
                    dictionary[nums[pos]] = pos
                    pos += 1
            else:
                    return [dictionary[target - nums[pos]], pos]

print(twoSums([2, 7, 11, 15]))
                    # Runtime: 44
                    # Memory Usage: 15.3 