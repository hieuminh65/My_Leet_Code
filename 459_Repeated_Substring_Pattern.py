class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 1:
            return False
        for i in range(1, len(s)):
            tempS = s[:i]
            print(tempS)
            key = 0
            for j in range(i, len(s), i):
                if s[j:j+i] != tempS:
                    key = 1
                    break
            if key == 0:
                return True
                
        return False

        


s = Solution()
print(s.repeatedSubstringPattern("bb"))