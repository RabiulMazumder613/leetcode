# My Solution: (Fast) Time Complexity O(n) | Space Complexity O(n)
# Time complexity: O(n). We traverse the list containing nn elements only once. Each lookup in the table costs only O(1) time.
# Space complexity: O(n). The extra space required depends on the number of items stored in the hash table, which stores at most n elements.
# Doesn't need return [] at the end since the problem states: You may assume that each input would have exactly one solution...
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, elem in enumerate(nums):
            potentialMatch = target - elem
            
            if potentialMatch in seen:
                return [seen[potentialMatch], index]
            else:
                seen[elem] = index
                
# Leetcode Solution: (Fast) Time Complexity O(n) | Space Complexity O(n)
# Same logic but uses "for i in range(len(nums))" to iterate over the elements in nums instead of enumerate
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
