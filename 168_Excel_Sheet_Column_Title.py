class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        excel = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        res = []
        while columnNumber != 0:
            print(columnNumber)
            letter = columnNumber % 26
            # print(letter)
            res.insert(0, excel[letter - 1])
            columnNumber = columnNumber // 26

        return "".join(res)

s = Solution()
print(s.convertToTitle(701)) # Expected: "ZY"

print(700//26)