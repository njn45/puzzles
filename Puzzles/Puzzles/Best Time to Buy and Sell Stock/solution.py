"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

 

Constraints:

    1 <= prices.length <= 10^5
    0 <= prices[i] <= 10^4

"""

class Solution:

    def max_profit(prices:list[int]) -> int:
        buy, profit = 0, 0 # two pointers, starting at idx 0

        for sell in range(1,len(prices)): # buy starts at idx 1 so we dont travel back in time
            if prices[buy] < prices[sell]:
                profit = max(profit, prices[sell] - prices[buy])
            else:
                buy = sell # if the buy price >= sell price, we have found a new lowest buy price so we need to move that pointer
        
        return profit

def main():
    assert Solution.max_profit([7,1,5,3,6,4]) == 5
    assert Solution.max_profit([7,6,4,3,1]) == 0
    assert Solution.max_profit([1,2,3,4,5,6,7]) == 6
    assert Solution.max_profit([1,1,1,1,1,1]) == 0
    assert Solution.max_profit([1]) == 0
    assert Solution.max_profit([72, 88, 57, 33, 36, 56, 91, 97, 57, 42, 40, 97, 53, 93, 83, 39, 97, 30, 3, 7]) == 64

if __name__ == "__main__":
    main()