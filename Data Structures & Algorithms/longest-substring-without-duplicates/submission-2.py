'''
s = "zxyzxyz"
        
use an 'index dict' to determine the latest occurance of a character 
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, indexDict = 0, {} 
        res = 0
        for right in range(len(s)): 
            if s[right] in indexDict: 
                left = max(left, indexDict[s[right]] + 1) # xxxx case: use the indexDict to update left to the most current occurance of the character 
            indexDict[s[right]] = right 
            res = max(res, right - left + 1)
    
        return res 