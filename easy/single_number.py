# https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_res = nums[0]
        
        for i in range(1, len(nums)):
            xor_res ^= nums[i]
            
        return(xor_res)
        