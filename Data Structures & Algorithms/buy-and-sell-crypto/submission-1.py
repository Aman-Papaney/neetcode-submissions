class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit : int = 0
        temp : int = prices[0]

        for i in prices:
            if (i - temp) > max_profit:
                max_profit = i - temp
            temp = min(temp, i)

        return max_profit