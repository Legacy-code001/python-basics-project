def count_ways(amount: int, coins:list[int]) -> int :
    result = {}

    def search(current_amount: int, coin_index: int):
        state = (current_amount, coin_index)
        if state in result:
            return result[state]

        if current_amount == 0:
            return 1

        if current_amount < 0 or coin_index >= len(coins):
            return 0

        use_coin = search(current_amount - coins[coin_index], coin_index)

        skip_coin = search(current_amount, coin_index + 1)

        result[state] = use_coin + skip_coin

        return result[state]
    
    return search(amount, 0)

print(count_ways(5, [1, 2, 5])) 
 



