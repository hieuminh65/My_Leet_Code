def isSubsequence(s: str, t: str) -> bool:
        if s == "":
            return True
        sP = tP = 0
        while tP < len(t) and sP < len(s):
            if t[tP] != s[sP]:
                tP+=1
            else:
                sP+=1
                tP+=1
        return sP > len(s) - 1

print(isSubsequence("b", "abc"))