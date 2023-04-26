def isValid(s):
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            print(c)
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack
s = "([)]"
print(isValid(s))