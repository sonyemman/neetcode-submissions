class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r: 
            #skip non alphanumeric numbers 
            while l < r and not self.isAlphaNum(s[l]): 
                l += 1
                print(f"{l}")
            while l < r and not self.isAlphaNum(s[r]): 
                r -= 1
                print(f"{r}")

            if s[l].lower() != s[r].lower(): 
                return False 
            #if they are the same keep advancing 
            l+= 1
            r -=1 
        
        return True

    def isAlphaNum(self, c): 
        return (ord('A') <= ord(c) <= ord('Z') or 
        ord('a') <= ord(c) <= ord('z') or 
        ord('0') <= ord(c) <= ord('9'))