# My Solution (Fast) Time Complexity O(n) | Space Complexity: O(1)
# Time complexity : O(N) since we go through the string of length N two times.
# Space complexity : O(1) because English alphabet contains 26 letters.
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)
        
        for i in s:
            if(freq[i] == 1):
                return s.index(i)
        return -1
      
# Leetcode Solution: (Fast) Time Complexity O(n) | Space Complexity: O(1)
# This is slightly slower but still fast
class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1
