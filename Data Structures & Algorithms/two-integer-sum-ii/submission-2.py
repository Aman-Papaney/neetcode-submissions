class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Intended 2 Pointer approach
        small: int = 0
        large: int = len(numbers) - 1
        temp_sum: int = numbers[small] + numbers[large]

        while (temp_sum != target) and (small < large):
            if temp_sum > target:
                large -= 1
            else:
                small += 1
            temp_sum = numbers[small] + numbers[large]
        return [small + 1, large + 1]