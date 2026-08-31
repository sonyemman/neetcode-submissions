class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_stripped = self.stripString(s)  
        l, r = 0, len(s_stripped) - 1


        #two pointer 
        while l < r:
            if s_stripped[l] != s_stripped[r]: 
                return False 
            l, r = l + 1, r - 1 

        return True


    
    def isAlphaNum(self, c): 
        return c.isalnum()

    
    def stripString(self, s): 
        res = []
        for c in s: 
            if c != ' ' or  c != '?' or c != '!':
                if self.isAlphaNum(c): 
                    res.append(c.lower())
        
        print(''.join(res))
        return ''.join(res)
        