class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        print((s)[1:-1])
        return s in (s + s)[1:-1]

        




        


s = Solution()
print(s.repeatedSubstringPattern("abcabcabcabc"))