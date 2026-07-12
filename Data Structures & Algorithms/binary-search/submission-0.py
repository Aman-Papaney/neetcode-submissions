class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result : int = -1

        left : int = 0
        right : int = len(nums) - 1

        while (left <= right):
            mid : int = left + (right - left) // 2

            if(nums[mid] == target):
                return mid
            elif (nums[mid] < target):
                left = mid + 1
            else:
                right = mid - 1
            
        return result
