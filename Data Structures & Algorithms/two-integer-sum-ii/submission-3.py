class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers) - 1

        while left < right:
            temp_sum = numbers[left] + numbers[right]
            if (temp_sum) < target:
                left += 1
            elif temp_sum > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        return [0, 0]