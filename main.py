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
        '1': [[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)], 3],  # line 11
        '2': [[(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)], 3],  # line 12
        '3': [[(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)], 3],  # line 13
        '4': [[(3, 0), (3, 1), (3, 2), (3, 3), (3, 4)], 3],  # line 14
        '5': [[(4, 0), (4, 1), (4, 2), (4, 3), (4, 4)], 3],  # line 15

        '6': [[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)], 3],  # line 20 diags
        '7': [[(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 3],  # line 21

        '8': [[(0, 0), (0, 1), (0, 2), (0, 3)], 2], # line 6
        '9': [[(1, 0), (1, 1), (1, 2), (1, 3)], 2], # line 7
        '10': [[(2, 0), (2, 1), (2, 2), (2, 3)], 2], # line 8 
        '11': [[(3, 0), (3, 1), (3, 2), (3, 3)], 2], # line 9
        '12': [[(4, 0), (4, 1), (4, 2), (4, 3)], 2], # line 10 
        
        
        '13': [[(0, 0), (1, 1), (2, 2), (3, 3)], 2], # line 18 diags
        '14': [[(4, 0), (3, 1), (2, 2), (1, 3)], 2], # line 19 

        
        '15': [[(0, 0), (1, 1), (2, 2)], 1],  # line 16
        '16': [[(2, 0), (1, 1), (0, 2)], 1],  # line 17

        '17': [[(0, 0), (0, 1), (0, 2)], 1], # line 1
        '18': [[(1, 0), (1, 1), (1, 2)], 1], # line 2
        '19': [[(2, 0), (2, 1), (2, 2)], 1], # line 3
        '20': [[(3, 0), (3, 1), (3, 2)], 1], # line 4
        '21': [[(4, 0), (4, 1), (4, 2)], 1], # line 5

        

    }
    paid_lines = []

    def calc_pay(symbol, multiplier):
        print (f"multiplier is {multiplier}")
        paid = char_pay[symbol] * multiplier

        return paid

    def check_payout(grid):
        lineNum = 0
        paid = 0
        counted_coordinates = set()  # Track coordinates that have been counted

        for pay_line_key in sorted(pay_lines, key=lambda k: len(pay_lines[k][0]), reverse=True):
            pay_line = pay_lines[pay_line_key][0]
            lineNum += 1

            # Check if any coordinate in this pay line has already been counted
            if any(coord in counted_coordinates for coord in pay_line):
                continue

            symbols_on_line = [grid[row][col] for (row, col) in pay_line]

            if len(set(symbols_on_line)) == 1:  # All symbols on the line are the same
                symbol = symbols_on_line[0]
                
                linepay = calc_pay(symbol, pay_lines[pay_line_key][1])
                paid += linepay
                print(
                    f"Payout! You got a winning line with the symbol {symbol} with line {lineNum}. Pays ${linepay}"
                )

                # Remember this set of coordinates so we don't double-count smaller overlapping lines
                counted_coordinates.update(pay_line)

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
