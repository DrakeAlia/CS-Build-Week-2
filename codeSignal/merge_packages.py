# Given a package with a weight limit limit and an array of integers items of where each integer represents the weight of an item, 
# implement a function merge_packages that finds the first two items in the items array whose sum of weights equals the given weight limit limit.
# Your function should return a pair [i, j] of the indices of the item weights, ordered such that i > j. If such a pair doesn’t exist, return an empty array.

# Examples:
# Input: items = [4, 6, 10, 15, 16], limit = 21
# Output: [3, 1]
# Explanation: The weight of the items at indices 3 and 1 sum up to the specified limit.
# [execution time limit] 4 seconds (py3)

# [input] array.integer items

# A list of item weights.

# [input] integer limit

# The weight limit we're aiming for by merging two packages.

# [output] array.integer

# A pair of item indices indicating the two items that, when merged, reach the specified limit.

def merge_packages(items, limit):
    for idx, i in enumerate(items):
        diff = limit - i          
        if diff in items[idx+1:]:  
            for idx2, j in enumerate(items[idx + 1:]):
                if j == diff:
                    return [idx + idx2+1, idx]
    return []


# Other method:
# def merge_two_lists(a, b):
#     data = {}
#     for pair in a+b:
#         key, value = pair
#         data[key] = data.get(key, 0) + value        
#     sorted_data = sorted([[key, value] for key, value in data.items()])
#     return sorted_data
#     print(sorted_data)