def maxProfit(array):
    currentProfit = maximumProfit = 0
    for i in range(1, len(array)):
        currentProfit += array[i] - array[i-1]
        currentProfit = max(0, currentProfit)
        if currentProfit > maximumProfit:
            maximumProfit = currentProfit

    return maximumProfit

print(maxProfit([23171,21011,21123,21366,21013,21367])) # 356