stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(x):
    x = stock_prices[x-1]
    return x
    
def max_price(a, b):
    maxp = max(stock_prices[a-1:b-1])
    return maxp

def min_price(a, b):
    minp = min(stock_prices[a-1:b-1])
    return minp
    
print(price_at(3))
print(max_price(1,3))
print(min_price(1,3))