prices = 1

def maxProfit_bruteforce (prices):
   max_price = 0

   for i, price in enumerate(prices):
       for j in range(i, len(prices)):
           max_price = max(prices[j] - price, max_price)

   return

if '__name__' == '__main__':
    max_Profit_bruteforce(pries)
