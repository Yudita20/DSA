def buyAndSellStock(nums):
    max_profit = 0
    buy_price = nums[0]
    for i in range(1, len(nums)):
        max_profit = max(nums[i] - buy_price, max_profit)
        buy_price = min(buy_price, nums[i])

    return max_profit


arr = [7, 1, 5, 3, 3, 4]
print(buyAndSellStock(arr))