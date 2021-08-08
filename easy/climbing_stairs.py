# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        num_ways = [1, 2]
        
        if n == 1:
            return num_ways[0]
        
        if n == 2:
            return num_ways[1]
        
        for i in range(1, n-1):
            num_ways.append(num_ways[i] + num_ways[i-1])
            
        return num_ways[-1]