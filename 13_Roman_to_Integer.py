def romanToInt(s: str) -> int:
    Rmap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num = Rmap[s[-1]]
    for i in range(len(s) - 2, -1, -1):
        if Rmap[s[i]] < Rmap[s[i +1 ]]:
            num -= (Rmap[s[i]])
        else:
            num += Rmap[s[i]] 
    return num

# romanToInt("LVIII")
print(romanToInt("LVIIV")) # 60
print(romanToInt("LVIII")) # 58