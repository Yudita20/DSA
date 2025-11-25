def BuyAndSellStock(nums):
    max_profit = 0
    buy_price = nums[0]

    for i in range(1 , len(nums)):
        if nums[i] < buy_price:
            buy_price = min(buy_price, nums[i])

        else:
            profit = nums[i] - buy_price
            max_profit = max(profit , max_profit)

    return max_profit


num = [7,1,5,3,6,4]
# num = [7,6,4,3,1]
print(BuyAndSellStock(num))

#T(n) : O(n)
#S(n) : O(1)