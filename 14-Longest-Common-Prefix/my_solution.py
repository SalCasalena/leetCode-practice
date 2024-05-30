"""
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ""
        temp_prefix = ""

        for i in range(len(strs[0])):
            temp_prefix += strs[0][i]
            for item in strs:
                if item[0: i+1] == temp_prefix:
                    continue
                else:
                    return prefix
            prefix = temp_prefix
        return temp_prefix

data = ['daabc', 'aac', 'aac']
s = Solution()
print(s.longestCommonPrefix(data))
        