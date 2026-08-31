# "ababd"
# time: n^2 space: O(1)

# start = 0 res = 2
# l = 0
# r = 2
# i = 1
# s[l] = b
# s[r] = b


class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        res = 0
        for i in range(len(s)): 
            #odd case 
            l = r = i 

            while l >= 0 and r < len(s) and s[l] == s[r]: 
                if (r - l + 1) > res: 
                    res = (r - l) + 1
                    start = l
                l -= 1 
                r += 1 

            # even case  
            l = i 
            r = i + 1 
            while l >= 0 and r < len(s) and s[l] == s[r]: 
                if (r - l + 1) > res: 
                    res = (r - l) + 1
                    start = l
                l -= 1 
                r += 1 
    
        return s[start: start + res]