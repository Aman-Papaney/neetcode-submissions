class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low: int = 0
        high: int = len(matrix) * len(matrix[0]) - 1

        while (low <= high):
            mid = low + int((high - low) / 2)

            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            ele = matrix[row][col]
            
            if (ele == target):
                return True
            elif (ele < target):
                low = mid + 1
            else:
                high = mid - 1

        return False 