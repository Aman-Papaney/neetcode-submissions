class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def can_eating_rate_be(rate):
            count: int = 0

            for i in piles:
                # count += i // rate + 1 if i % rate != 0 else i // rate
                count += (i + rate - 1) // rate
            if count <= h:
                return True
            else:
                return False
        
        left: int = 1
        right: int = max(piles)

        ans_eating_rate: int = right

        while (left < right):
            mid: int = left + (right - left) // 2

            if (can_eating_rate_be(mid)):
                right = mid
                ans_eating_rate = min(ans_eating_rate, mid)
            else:
                left = mid + 1
        return int(ans_eating_rate)
    

            