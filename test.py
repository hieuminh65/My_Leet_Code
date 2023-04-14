def maxProfit(prices):
    maxP = 0
    l = 0
    r = 1
    while r < len(prices):
        if prices[r] > prices[l]:
            maxP = max(prices[r] - prices[l], maxP)
        else:
            l = r
        r += 1

    return maxP
print(maxProfit([7,1,5,3,6,4]))