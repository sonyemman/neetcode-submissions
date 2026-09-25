#.            r     l 
# Input: s = "racecar", t = "carrace"

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s or not t: 
            return False 

        if len(s) != len(t): 
            return False 
        
        s_sorted = sorted(s)
        t_sorted = sorted(t)

        if s_sorted == t_sorted: 
            return True
        return False  