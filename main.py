import random

# char_weights = {
# "10": 20,
# "J": 18,
# "Q": 16,
# "K": 14,
# "A": 12,
# "#": 10,
# "$": 8,
# "&": 7,
#    "W": 6,
# }

char_weights = {
    "$": 10,
    "#": 10,
    "!": 10,
}

char_pay = {
    "$": 5,
    "#": 10,
    "!": 15,
}

symbols = [symbol for symbol, weight in char_weights.items() for _ in range(weight)]

random_char = random.choice(symbols)
print("Chosen Symbol: ", random_char)


def play():
    rows = 3
    columns = 3
    grid = [[random.choice(symbols) for _ in range(columns)] for _ in range(rows)]

    # Define a few pay lines using (row, column) coordinates
    pay_lines = [
        # Straght across
        [(0, 0), (0, 1), (0, 2)],  # line 1
        [(1, 0), (1, 1), (1, 2)],  # line 2
        [(2, 0), (2, 1), (2, 2)],  # line 3
        # Diagonals
        [(0, 0), (1, 1), (2, 2)],  # line 4
        [(2, 0), (1, 1), (0, 2)],  # line 5
        # ... add all other pay lines here
    ]

    def calc_pay(symbol, count):
        count = 1
        paid = char_pay[symbol] * count
        return paid

    def check_payout(grid):
        lineNum = 0
        paid = 0
        for pay_line in pay_lines:
            lineNum = lineNum + 1
            symbols_on_line = [grid[row][col] for (row, col) in pay_line]
            if len(set(symbols_on_line)) == 1:  # All symbols on the line are the same
                linepay = calc_pay(symbols_on_line[0], 1)
                paid = paid + linepay
                print(
                    f"Payout! You got a winning line with the symbol {symbols_on_line[0]} with line {lineNum}. Pays ${linepay}"
                )
        print(f"Your total winnings are ${paid}")

    def print_grid(grid):
        # Determine the width of each cell
        cell_width = (
            max(len(item) for row in grid for item in row) + 2
        )  # 2 extra for padding
        border_length = len(grid[0]) * cell_width

        # Top border
        print("+" + "-" * border_length + "+")

        for row in grid:
            print("|", end="")
            for item in row:
                # Center each item within the cell width, padded by spaces
                print(item.center(cell_width), end="")
            print("|")  # Right border

        # Bottom border
        print("+" + "-" * border_length + "+")

    print("Good luck!")
    print_grid(grid)
    check_payout(grid)


play()
