# def spaceAndCapitalize(word):
#     word_arr = word.split(" ")

#     for i in range(len(word_arr)):
#         current_word = word_arr[i]
#         if current_word:
#             first_char = current_word[0]
#         if ord(first_char) >= 97 and ord(first_char) <= 122:
#             upperCase = ord(first_char) - 32

#             word_arr[i] = chr(upperCase) + current_word[1:]

#     return "".join(word_arr)

# print(spaceAndCapitalize("hello world from python"))


# # working things out

# def count_ways(amount: int, coins: list[int]) -> int:
#     # dp[i] will store the number of ways to make change for amount i
#     dp = [0] * (amount + 1) # [0,0,0,0,0,0]
    
#     # Base case: There is exactly 1 way to make an amount of 0 (using no coins)
#     dp[0] = 1
    
#     # Process each coin one by one to avoid duplicate combinations (e.g., 1+2 and 2+1)
#     for coin in coins:
#         for i in range(coin, amount + 1):
#             dp[i] += dp[i - coin]
            
#     return dp[amount]

# # --- Quick Test ---
# # Making 5 out of coins [1, 2, 5]
# # Combinations: (1*5), (1*3 + 2), (1 + 2*2), (5) -> 4 ways
# print(count_ways(5, [1, 2, 5]))  # Output: 4



def count_ways(amount: int, coins: list[int]) -> int:
    # A dictionary to store previously calculated results: (current_amount, coin_index) -> result
    memo = {}

    def db_search(current_amount: int, coin_index: int) -> int:
        # 1. Check if we already calculated this specific state
        state = (current_amount, coin_index)
        if state in memo:
            return memo[state]

        # 2. Base Case: Successfully made exact change
        if current_amount == 0:
            return 1

        # 3. Base Case: Went over budget or ran out of coins
        if current_amount < 0 or coin_index >= len(coins):
            return 0

        # Choice A: Use the coin (subtract its value, keep the same index to reuse it)
        use_coin = db_search(current_amount - coins[coin_index], coin_index)

        # Choice B: Skip the coin (keep amount, move to the next coin type)
        skip_coin = db_search(current_amount, coin_index + 1)

        # 4. Save the result in our manual cache and return it
        memo[state] = use_coin + skip_coin
        return memo[state]

    return db_search(amount, 0)
print(count_ways(5, [1,2,5]))