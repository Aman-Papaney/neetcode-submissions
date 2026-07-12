class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        right = k - 1
        ans = []
        
        for left in range(len(nums) - k + 1):
            ans.append(max(nums[left:right + 1]))
            right += 1
        return ans