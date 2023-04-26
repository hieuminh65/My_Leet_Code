class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) <=1 :
            return int(tokens[0])
        stack =[]
        operand = ("+", "-", "*", "/")

        res = 0
        for c in tokens:
            if c in operand:
                if c == operand[0]:
                    res = self.add(stack[-2], stack[-1])
                elif c == operand[1]:
                    res = self.sub(stack[-2], stack[-1])
                elif c == operand[2]:
                    res = self.mul(stack[-2], stack[-1])
                elif c == operand[3]:
                    res = self.div(stack[-2], stack[-1])
                stack.pop()
                stack.pop()
                stack.append(res)
                continue
            stack.append(c)
        return int(res) 
    def add(self,x,y):
        return int(x)+int(y)
    def sub(self,x,y):
        return int(x)-int(y)
    def mul(self,x,y):
        return int(x)*int(y)
    def div(self,x,y):
        return int(x)/int(y)