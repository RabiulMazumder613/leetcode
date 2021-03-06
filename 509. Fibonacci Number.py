#Fibonacci Sequence : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 . . .

# Recursive Method: VERY SLOW
# O(2^n) time | O(n) space
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)     
        
# Recursive fibonacci + memorization (dictionary) + Top Down
# O(n) time | O(n) space    
class Solution:
    def __init__(self):
        self.cache = {0:0, 1:1}
    def fib(self, n: int) -> int:
        if n in self.cache: 
            return self.cache[n]
        else:
            self.cache[n] = self.fib(n-1) + self.fib(n-2)
            return self.cache[n]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ THESE SOLTUIONS ARE ALL VARIATIONS OF THE SAME THING ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~       
        
# Bottom Up Method: Iterative
# If...Else... at the return statement
# O(n) time | O(1) space
class Solution:
    def fib(self, n: int) -> int:
        cache = [0,1]
        for i in range(2, n+1):
            cache.append(cache[0] + cache[1])
            del cache[0]
        return cache.pop() if n >= 1 else cache[0]  
      
# Bottom Up Method: Iterative
# If...Else... at the beginning 
# O(n) time | O(1) space      
class Solution:
    def fib(self, n: int) -> int:
        cache = [0,1]
        if n == 0:
            return cache[0]
        else:
            for i in range(2, n+1):
                cache.append(cache[0] + cache[1])
                del cache[0]
            return cache.pop()      
          
# ALTERNATIVE Bottom Up Method: Iterative
# Swapping
# O(n) time | O(1) space    
class Solution:
    def fib(self, n: int) -> int:
        a,b = 0,1
        for i in range(n):
            a, b = b, a+b
        return a       
    
# ALTERNATIVE Bottom Up Method: Iterative
# More explicit Swapping
# If...Else... at the return statement
# O(n) time | O(1) space          
class Solution:
    def fib(self, n: int) -> int:
        lastTwo = [0,1]
        for i in range(2,n+1):
            nextFib = lastTwo[0] + lastTwo[1]
            lastTwo[0] = lastTwo[1]
            lastTwo[1] = nextFib
        return lastTwo[1] if n >= 1 else lastTwo[0]        

# ALTERNATIVE Bottom Up Method: Iterative
# More explicit Swapping 
# If...Else... at the beginning 
# O(n) time | O(1) space     
class Solution:
    def fib(self, n: int) -> int:
        lastTwo = [0,1]
        if n == 0:
            return lastTwo[0]
        else:
            for i in range(2,n+1):
                nextFib = lastTwo[0] + lastTwo[1]
                lastTwo[0] = lastTwo[1]
                lastTwo[1] = nextFib
            return lastTwo[1]           
