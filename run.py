import random

class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = [['O' for _ in range(size)] for _ in range(size)]

    def display(self):
        print("   " + " ".join([chr(i + ord('A')) for i in range(self.size)]))
        for i, row in enumerate(self.grid):
            print(f"{i + 1:2} {' '.join(row)}")

class Ship:
    def __init__(self, size):
        self.size = size
        self.coordinates = []

    def place_ship(self, grid):
        while True:
            try:
                position = input(f"Enter the starting position for your {self.size}-length ship (e.g., A1): ")
                col = ord(position[0].upper()) - ord('A')
                row = int(position[1:]) - 1

                orientation = input("Enter the orientation (H for horizontal, V for vertical): ").upper()

                if orientation == 'H':
                    if col + self.size <= grid.size:
                        self.coordinates = [(col + i, row) for i in range(self.size)]
                        break
                    else:
                        print("Invalid placement. Ship goes beyond the grid.")
                elif orientation == 'V':
                    if row + self.size <= grid.size:
                        self.coordinates = [(col, row + i) for i in range(self.size)]
                        break
                    else:
                        print("Invalid placement. Ship goes beyond the grid.")
                else:
                    print("Invalid orientation. Please enter 'H' or 'V'.")

            except (ValueError, IndexError):
                print("Invalid input. Please try again.")

        for coord in self.coordinates:
            if grid.grid[coord[1]][coord[0]] == 'O':
                grid.grid[coord[1]][coord[0]] = 'S'
            else:
                print("Invalid placement. Ships overlap.")
                self.place_ship(grid)

class BattleshipGame:
    def __init__(self, size):
        self.user_grid = Grid(size)
        self.computer_grid = Grid(size)
        self.user_ships = [Ship(3) for _ in range(3)]
        self.computer_ships = [Ship(3) for _ in range(3)]

    def user_place_ships(self):
        print("Welcome to Battleship!")
        self.user_grid.display()

        for ship in self.user_ships:
            ship.place_ship(self.user_grid)
            self.user_grid.display()

    def computer_place_ships(self):
        for ship in self.computer_ships:
            while True:
                col = random.randint(0, self.computer_grid.size - 1)
                row = random.randint(0, self.computer_grid.size - 1)

                orientation = random.choice(['H', 'V'])

                if orientation == 'H' and col + ship.size <= self.computer_grid.size:
                    ship.coordinates = [(col + i, row) for i in range(ship.size)]
                    break
                elif orientation == 'V' and row + ship.size <= self.computer_grid.size:
                    ship.coordinates = [(col, row + i) for i in range(ship.size)]
                    break

        print("Computer has placed its ships.")

    def user_attack(self):
        while True:
            try:
                target = input("Enter target (e.g., A1): ")
                col = ord(target[0].upper()) - ord('A')
                row = int(target[1:]) - 1

                if 0 <= col < self.computer_grid.size and 0 <= row < self.computer_grid.size:
                    if self.computer_grid.grid[row][col] == 'O':
                        print("You missed!")
                        self.computer_grid.grid[row][col] = 'X'
                        break
                    elif self.computer_grid.grid[row][col] == 'S':
                        print("You hit a ship!")
                        self.computer_grid.grid[row][col] = 'X'
                        break
                    elif self.computer_grid.grid[row][col] == 'X':
                        print("You already targeted this position. Try again.")
                    else:
                        print("Invalid target. Try again.")
                else:
                    print("Invalid target. Try again.")

            except (ValueError, IndexError):
                print("Invalid input. Please try again.")

    def computer_attack(self):
        while True:
            col = random.randint(0, self.user_grid.size - 1)
            row = random.randint(0, self.user_grid.size - 1)

            if self.user_grid.grid[row][col] == 'O':
                print(f"Computer missed at {chr(col + ord('A'))}{row + 1}.")
                self.user_grid.grid[row][col] = 'X'
                break
            elif self.user_grid.grid[row][col] == 'S':
                print(f"Computer hit your ship at {chr(col + ord('A'))}{row + 1}!")
                self.user_grid.grid[row][col] = 'X'
                break

    def is_game_over(self):
        return all(all(cell == 'X' or cell == 'S' for cell in row) for row in self.user_grid.grid) or \
               all(all(cell == 'X' or cell == 'S' for cell in row) for row in self.computer_grid.grid)

    def play(self):
        self.user_place_ships()
        self.computer_place_ships()

        while not self.is_game_over():
            self.user_grid.display()
            self.user_attack()

            if self.is_game_over():
                print("Congratulations! You won!")
                break

            self.computer_attack()

            if self.is_game_over():
                print("Computer wins! Better luck next time.")

if __name__ == "__main__":
    game = BattleshipGame(size=8)
    game.play()