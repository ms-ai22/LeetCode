class Solution:
    def climbStairs(self, n: int) -> int:
        step_ways = {1:1, 2:2}
        for i in range(3,n+1):
            step_ways[i] = step_ways[i-1] + step_ways[i-2]
        return step_ways[n]
                
