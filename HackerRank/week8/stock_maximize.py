import math


def stockmax(prices):
    profit = 0
    highest = -math.inf
    for i in range(len(prices) -1, -1, -1):

        if prices[i] > highest:
            highest = prices[i]
        elif prices[i] < highest:
            profit += highest - prices[i]

    return profit











print(stockmax([5, 3, 2]))
print(stockmax([1, 2, 100]))
print(stockmax([1, 3, 1, 2]))
