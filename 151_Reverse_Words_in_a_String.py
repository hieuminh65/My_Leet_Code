class Solution:
    def reverseWords(self, s: str) -> str:
        p = len(s) - 1
        stack = []
        word = ""
        while p >= 0:
            if s[p] == " " and not stack:
                p-=1
                continue
            elif s[p] == " " and stack:
                
                while stack:
                    word += stack.pop()
                word += " "
            else:
                stack.append(s[p])
            p-=1

        while stack:
            word += stack.pop()
        if word[-1] == " ":
            word = word[:-1]
        return word
            