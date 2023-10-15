import random


char_weights = {
    "10": 20,
    "J": 18,
    "Q": 16,
    "K": 14,
    "A": 12,
    "#": 10,
    "$": 8,
    "&": 7,
    "W": 6,
}

symbols = [symbol for symbol, weight, in char_weights.items() for _ in range(weight)]

random_char = random.choice(symbols)
print("Chosen Symbol: ", random_char)


def play():
    rows = 5
    columns = 5
    grid = [[random.choice(symbols) for _ in range(columns)] for _ in range(rows)]

    def check_payout(grid):
        for row in grid:
            consecutive_count = 1
            prev_symbol = row[0]  # Symbol in the first column
            for symbol in row[1:]:
                if symbol == prev_symbol:
                    consecutive_count += 1
                else:
                    consecutive_count = 1
                    prev_symbol = symbol
                if consecutive_count >= 2:
                    print(f"Payout! You got {consecutive_count} {symbol}(s) in a row!")

    # Transpose the grid to work with columns
    column_grid = list(map(list, zip(*grid)))

    # Check for payouts in columns
    for column in column_grid:
        if len(set(column)) == 1:
            symbol = column[0]
            print(f"Payout! You got {len(column)} {symbol}(s) in a row!")

    print("Good luck!")
    print_grid(grid)

    check_payout(grid)


def print_grid(grid):
    for row in grid:
        for item in row:
            print(item, end="\t")
        print()


play()
