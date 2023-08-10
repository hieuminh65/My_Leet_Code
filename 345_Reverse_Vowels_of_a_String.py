class Solution:
    def reverseVowels(self, s: str) -> str:

        l,r = 0, len(s) - 1
        s = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        while l < r:
            while s[l] not in vowels and l < r:
                l+=1
            while s[r] not in vowels and r > l:
                r-=1
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            print(s)
            print(l, r)
            print(s[l], s[r])
            l+=1
            r-=1
        res = ""

        for l in s:
            res += l
        return res

s = Solution()
print(s.reverseVowels("leetcode"))