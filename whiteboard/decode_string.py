# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
# Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 
# For example, there won't be input like 3a or 2[4].
 
# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
# Example 4:

# Input: s = "abc3[cd]xyz"
# Output: "abccdcdcdxyz"

# class Solution:
    # def decodeString(self, s: str) -> str:
def decodeString(s):
        res = ""
        i = 0
        while i < len(s):
            if s[i].isdigit():
                for j in range(i, len(s)):
                    if not s[j].isdigit():
                        scalar = int(s[i:j])
                        break

                stack_count = 1
                start_sub = j + 1
                
                for j in range(start_sub, len(s)):
                    if s[j] == '[':
                        stack_count += 1
                    elif s[j] == ']':
                        stack_count -= 1
                        if stack_count == 0:
                            end_sub = j
                            break

                sub_dec = self.decodeString(s[start_sub:end_sub])
                res += scalar * sub_dec
                i = j + 1
            else:
                res += s[i]
                i += 1

        return res

# Runtime: 24 ms
# Memory Usage: 13.6 MB
        