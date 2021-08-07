# My Initial Solution: (Very Slow)
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hold = []
        for i in nums:
            if i not in hold:
                hold.append(i)
            else:
                return True
        return False
    
    
# Better Version of Mine:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for num in nums:
            if num in visited:
                return True
            else:
                visited.add(num)
        return False
    
# With Dictionary:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = {}
        for num in nums:
            if num in visited:
                return True
            else:
                visited[num] = 1 # 1 can be anything. Could even use True
        return False
    
# One-liner Solution:
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
