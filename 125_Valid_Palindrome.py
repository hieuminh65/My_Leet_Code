class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) -1

        while l < r:
            
            while not self.isValid(s[l]) and l<r:
                l+=1
            while not self.isValid(s[r]) and r>l:
                r -=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1

        return True
    def isValid(self, c):
        return c >= 'a' and c <= 'z' or c >= 'A' and c <= 'Z' or c >= '0' and c <= '9'
    
s = "A man, a plan, a canal: Panama"
s1 = ".,"
s2 = ".a,"

So = Solution()
print(So.isPalindrome(s1))