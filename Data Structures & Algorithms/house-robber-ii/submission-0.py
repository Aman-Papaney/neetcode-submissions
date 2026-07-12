class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        

        def dfs(temp):
            if not temp:
                return 0
            if len(temp) == 1:
                return temp[0]

            dp = [0] * len(temp)
            dp[0] = temp[0]
            dp[1] = max(temp[0], temp[1])

            for i in range(2, len(temp)):
                dp[i] = max(dp[i - 1], temp[i] + dp[i - 2])

            return dp[-1]
        
        return max(dfs(nums[1:]), dfs(nums[:-1]))