class Trader:
    def __init__(self, prices):
        self.prices = prices

    def predict(self):
        least_price = max(self.prices)
        max_profit = 0

        for price in self.prices:
            if price < least_price:
                least_price = price

            max_profit = max(max_profit, price-least_price)

        return max_profit