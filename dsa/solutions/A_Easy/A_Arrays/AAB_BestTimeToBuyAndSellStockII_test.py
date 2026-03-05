import pytest

from python.A_Easy.A_Arrays.AAB_BestTimeToBuyAndSellStockII import best_time_to_buy_and_sell

CASES = [
    ([7, 1, 5, 3, 6, 4], 7),
    ([1, 2, 3, 4, 5], 4),
    ([7, 6, 4, 3, 1], 0),
    ([1], 0),
    ([], 0),
    ([1, 10, 7], 9),
    ([1, 10, 7, 10], 12),
    ([2, 2, 2], 0),
    ([2, 2], 0),
    ([2, 2, 2, 2, 10, 2, 2, 10], 16)
]

@pytest.mark.parametrize("prices,expected", CASES)
def test_best_time_to_buy_and_sell(prices, expected):
    assert best_time_to_buy_and_sell(prices) == expected
