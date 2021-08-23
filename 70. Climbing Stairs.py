# Top down Recursive - Time Limit Exceeded
# VERY SLOW 
# O(2^n) time | O(n) space
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)
      
# Top down Recursive + memorization (dictionary)   
# O(n) time | O(n) space    
class Solution:
    def __init__(self):
        self.dic = {1:1, 2:2}
    def climbStairs(self, n: int) -> int:
        if n not in self.dic:
            self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dic[n]      
      
# Bottom up
# O(n) time | O(1) space     
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        a, b = 1, 2
        for i in range(2, n):
            tmp = b
            b = a+b
            a = tmp
        return b      
      
# O(n) time | O(1) space         
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [1,2]
        for i in range(2, n):
            cache.append(cache[0] + cache[1])
            del cache[0]
        return cache.pop() if n > 1 else cache[0]      
     
# O(n) time | O(1) space        
class Solution:
    def climbStairs(self, n: int) -> int:
        a,b = 1,1
        for i in range(n):
            a, b = b, a+b
        return a      
