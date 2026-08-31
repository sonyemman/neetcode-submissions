'''
1. scope the problem 
 
output = "AWDRS

- if not all letters in s is in t - then return "" 
- if t is "" return "" - edge case 

2. algorithm 
- brute force - go through evry substring and seee if AWS (chars of t is in it) n^2 to n^3 
- optomized solution - sliding window - check if dict window has all characters in t 
- if you find the window - shrink the window to find minimum
- grow window untill all chars in t is in the window 
'''
from collections import defaultdict 
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if not t:
            return ""
        
        countT, window = defaultdict(int), defaultdict(int)

        for c in t: 
            countT[c] += 1

        res = [-1, -1] 
        resLen = float('inf')
        l = 0
        have, need = 0, len(countT) 

        for r in range(len(s)): 
            c = s[r] 
            window[c] += 1

            if c in countT and window[c] == countT[c]: 
                have += 1

            while have == need: 
                if (r - l + 1) < resLen: 
                    resLen = (r - l + 1)
                    res = [l , r]

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]: 
                    have -= 1
                l += 1 

        l, r = res
        return s[l: r + 1] if resLen != float('inf') else "" 
# s = "AAWDRSD" t ="AAWS


        
        

        