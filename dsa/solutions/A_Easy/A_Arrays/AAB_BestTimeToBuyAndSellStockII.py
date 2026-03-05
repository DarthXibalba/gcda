def best_time_to_buy_and_sell(prices):
    profit = 0
    i = 0
    j = i + 1
    
    while j < len(prices):
        if prices[i] < prices[j]:
            profit += prices[j]-prices[i]
        i += 1
        j += 1

    return profit
