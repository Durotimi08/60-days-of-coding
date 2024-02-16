class CoinDispenser:
    def __init__(self, coins):
        self.coins = sorted(coins, reverse=True)

    def dispense(self, amount):
        coin_table = [0] + [float("inf") for _ in range(amount)]

        for unit_amount in range(1, amount+1):
            for coin in self.coins:
                if unit_amount == coin:
                    coin_table[unit_amount] = 1
                    break

                if unit_amount > coin:
                    coin_table[unit_amount] = min(coin_table[unit_amount], coin_table[unit_amount-coin]+1)

        return coin_table[amount] if coin_table[amount] < float("inf") else -1
