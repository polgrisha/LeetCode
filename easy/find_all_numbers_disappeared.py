# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i, num in enumerate(nums):
            right_num = abs(num)
            if nums[right_num-1] > 0:
                nums[right_num-1] = -nums[right_num-1]
        
        output = []
        
        for i, num in enumerate(nums):
            if num > 0:
                output.append(i+1)
                
        return(output)
        