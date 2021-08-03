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
    
# Fastest Solution:
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
