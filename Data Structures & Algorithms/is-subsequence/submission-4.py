"""
brute force solution 
loop through every letter in s to find a match 
for s = node and t = neetcode 
for n -> loop through t to find an n
for o -> loop through t to find an o 
and so on, so this is a n^2 
optomization: 
1. 2 pointer solution 
start a pointer and advance the point when you see a match 


"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1, p2 = 0, 0 

        
            
        while p1 < len(s) and p2 < len(t): 
            if s[p1] == t[p2]: 
                p1 = p1 + 1
            p2 = p2 + 1 
        

        

        return p1 == len(s)