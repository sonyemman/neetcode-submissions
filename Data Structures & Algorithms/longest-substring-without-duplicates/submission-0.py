class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indexDict = {} 
        left = 0 
        res = 0 

        for right in range(len(s)): 
            if s[right] in indexDict: 
                left = max(indexDict[s[right]] + 1, left)
            indexDict[s[right]] = right
            res = max(right - left + 1, res)

        return res 

        