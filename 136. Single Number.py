# My Solution: Time Complexity O(n) | Space Complexity: O(n)
from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = Counter(nums)
        
        for i in nums:
            if(freq[i]==1):
                return i
         
