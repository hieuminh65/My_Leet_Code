from collections import deque
import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: [TreeNode]) -> int:
        level = 1
        Sum = 0
        currentLevel = 1
        q = []

        q.append(root)
        sumLevel = -math.inf
        while q:
            if sumLevel > Sum:
                    Sum = sumLevel
                    level = currentLevel
            sumLevel = 0
            currentLevel +=1   
            for _ in range(len(q)):
                print(sumLevel)
                node = q.pop(0)
                sumLevel += node.val
                

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return level

s = Solution()
# [-100,-200,-300,-20,-5,-10,null]
root = TreeNode(-100)
root.left = TreeNode(-200)
root.right = TreeNode(-300)
root.left.left = TreeNode(-20)
root.left.right = TreeNode(-5)
root.right.left = TreeNode(-10)
print(s.maxLevelSum(root))