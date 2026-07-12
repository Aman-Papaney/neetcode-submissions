class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def ans(on_step):
            if on_step > n:
                return 0
            if on_step == n:
                return 1

            if memo.get(on_step):
                return memo[on_step]
            
            temp = ans(on_step + 1) + ans(on_step + 2)
            memo[on_step] = temp
            return temp
            
        return ans(0)