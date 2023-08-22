class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []


        for n in asteroids:

            while stack and stack[-1] > 0 and n < 0:
                # print(stack)
                lastE = stack[-1]
                if lastE + n > 0:
                    break
                elif lastE + n < 0:
                    stack.pop()
                else:
                    stack.pop()
                    break
            else:
                stack.append(n)
        return stack
    
s = Solution()
asteroids = [-2,-2,1,-2] # Expected: [-2,-2,-2]
print(s.asteroidCollision(asteroids))