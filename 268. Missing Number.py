# My Brute Force Solution: (Very Slow)
# Even with using nums.sort() still very slow
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for n in range(len(nums) + 1):
            if n not in nums:
                return n
              
# HashSet (Faster) Time Complexity O(n) | Space Complexity: O(n)
# By inserting each element of nums into a set
# it allows us to later query for containment in O(1) time.
class Solution:
    def missingNumber(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number

# Video Explaination Link: https://www.youtube.com/watch?v=i0WwsQYrMAM
