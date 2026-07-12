class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Classic 2 sum approach
        temp = {}

        for i in range(1, len(numbers) + 1):
            if (target - numbers[i - 1]) in temp.keys():
                return [temp[target - numbers[i - 1]], i]
            else:
                temp[numbers[i - 1]] = i
