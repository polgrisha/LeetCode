# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        to_xor = len(nums)
        
        for i, num in enumerate(nums):
            to_xor ^= i ^ num
            
        return to_xor