# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        used_nums = dict()
        
        flag = False
        
        for num in nums:
            if num in used_nums:
                flag = True
                break
            used_nums[num] = 1
            
        if flag:
            return True
        else:
            return False