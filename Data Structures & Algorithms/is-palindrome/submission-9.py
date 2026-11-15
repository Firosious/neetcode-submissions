class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) -1
        s = s.lower()

        while l < r:
            if not self.isAlpha(s[l]):
                l+=1
                continue
            if not self.isAlpha(s[r]):
                r-=1
                continue
            
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
        return True
    
    def isAlpha(self, c: str):
        return (ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))