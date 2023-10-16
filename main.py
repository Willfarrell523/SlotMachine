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
    rows = 5
    columns = 5
    grid = [[random.choice(symbols) for _ in range(columns)] for _ in range(rows)]

    # Define a few pay lines using (row, column) coordinates
    pay_lines = {
        # Straght across
        '1': [[(0, 0), (0, 1), (0, 2)], 1],  # line 1
        '2': [[(1, 0), (1, 1), (1, 2)], 1],  # line 2
        '3': [[(2, 0), (2, 1), (2, 2)], 1], # line 3
        '4': [[(3, 0), (3, 1), (3, 2)], 1], # line 4
        '5': [[(4, 0), (4, 1), (4, 2)], 1], # line 5

        '6': [[(0, 0), (0, 1), (0, 2), (0, 3)], 2], # line 6
        '7': [[(1, 0), (1, 1), (1, 2), (1, 3)], 2], # line 7
        '8': [[(2, 0), (2, 1), (2, 2), (2, 3)], 2], # line 8 
        '9': [[(3, 0), (3, 1), (3, 2), (3, 3)], 2], # line 9
        '10': [[(4, 0), (4, 1), (4, 2), (4, 3)], 2], # line 10 

        '11': [[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)], 3],  # line 
        '12': [[(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)], 3],  # line 
        '13': [[(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)], 3],  # line 
        '14': [[(3, 0), (3, 1), (3, 2), (3, 3), (3, 4)], 3],  # line 
        '15': [[(4, 0), (4, 1), (4, 2), (4, 3), (4, 4)], 3],  # line 

        # Diagonals
        '16': [[(0, 0), (1, 1), (2, 2)], 1],  # line 
        '17': [[(2, 0), (1, 1), (0, 2)], 1],  # line 
        
        '18': [[(0, 0), (1, 1), (2, 2), (3, 3)], 2],
        '19': [[(4, 0), (3, 1), (2, 2), (1, 3)], 2],

        '20': [[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)], 3],  # line 
        '21': [[(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 3],  # line 
    
    }

    def calc_pay(symbol, count):
        
        paid = char_pay[symbol] * count
        return paid

    def check_payout(grid):
        
        paid = 0
        for lineNum, line_data in pay_lines.items():
            pay_line, multiplier = line_data
            symbols_on_line = [grid[row][col] for (row, col) in pay_line]
            if len(set(symbols_on_line)) == 1:  # All symbols on the line are the same
                linepay = calc_pay(symbols_on_line[0], multiplier)
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
