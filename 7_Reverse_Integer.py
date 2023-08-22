def reverse(x: int) -> int:
        res = 0
        i = 0
        while x != 0:
            res += (x % 10) * ((10**i) * res)
            x = x // 10
            i += 1
        return res

print(reverse(123))