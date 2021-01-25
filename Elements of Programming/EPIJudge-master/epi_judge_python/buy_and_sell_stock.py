from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    max_earnings = 0
    buy = prices[0]
    for i in range(1, len(prices)):
        max_earnings = max(max_earnings, prices[i] - buy)
        buy = min(buy, prices[i])
    return max_earnings

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
    #buy_and_sell_stock_once([0.3, 0.2, 0.3])
