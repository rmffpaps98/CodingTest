def solution(price):
    return int(price * 0.95) if 100000 <= price and price < 300000 else int(price * 0.9) if 300000 <= price and price < 500000 else int(price * 0.8) if price >= 500000 else price