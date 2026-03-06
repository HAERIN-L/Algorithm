def solution(price):
    discount = {500000:0.8, 300000:0.9, 100000:0.95}
    
    for limit, rate in discount.items():
        if price >= limit:
            return int(price*rate)
    return price