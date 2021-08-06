# Initital Solution: It works but when the input size is immense it is REALLY SLOW
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(1, len(nums)+1):
            if i not in nums:
                ans.append(i)
        return ans
      
# Updated Solution: (Fast) Time Complexity O(n) | Space Complexity: O(n)
# This was faster because it transformed the input list into a set 
# Link to why Set is faster at finding than with Lists: https://stackoverflow.com/questions/8929284/what-makes-sets-faster-than-lists
# The time complexity of list to set conversion is O(n) and find num in set is O(1)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        setNums = set(nums)
        n = len(nums) + 1
        
        for i in range(1, n):
            if i not in setNums:
                ans.append(i)
        
        return ans

# Ideal Solution: (Fast) Time Complexity O(n) | Space Complexity: O(1)      
# This is with O(1) space as the question gives a follow up to increase the difficulty
# Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
# Link to Solution: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/344583/Python%3A-O(1)-space-solution
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            if nums[temp] > 0:
                nums[temp] *= -1
        
        res = []
        for i,n in enumerate(nums):
            if n > 0:
                res.append(i+1)
        
        return res
