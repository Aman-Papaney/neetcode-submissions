class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left: int = 0
        right: int = len(heights) - 1
        answer = area = 0
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)

            if (heights[left] < heights[right]):
                left += 1
            else:
                right -= 1
            
            answer = max(area, answer)
        
        return answer
