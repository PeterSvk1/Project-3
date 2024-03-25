# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


# Beggining of the code for the project 3: BATTLESHIPS project
from random import randint

class BattleshipGame:
    def __init__(self):
        self.player_name = ""
        self.rows = 0
        self.cols = 0
        self.player_board = []
        self.opponent_board = []
        self.player_score = 0
        self.opponent_score = 0
        self.previous_guesses = set()

    def create_board(self, rows, cols):
        return [["O" for _ in range(cols)] for _ in range(rows)]

    def get_board_size(self):
        while True:
            try:
                self.rows = int(input("Please enter how many rows you want between 3 and 8: "))
                if 3 <= self.rows <= 8:
                    break
                else:
                    print("Please enter how many rows you want between 3 and 8.")
            except ValueError:
                print("Please enter number between 3 and 8.")

        while True:
            try:
                self.cols = int(input("Please enter how many columns you want between 3 and 8: "))
                if 3 <= self.cols <= 8:
                    break
                else:
                    print("Please enter how many columns you want between 3 and 8")
            except ValueError:
                print("Please enter number between 3 and 8.")
    
    def setup_game(self):
               self.get_board_size()
               self.player_board = self.create_board(self.rows, self.cols)
               self.opponent_board = self.create_board(self.rows, self.cols)
   
    def print_boards(self):
        print(f"{self.player_name} board:")
       
        for row in self.player_board:
            print(" ".join(row))
            print("Computer:")
        for row in self.opponent_board:
            print(" ".join(["O" if cell != "X" and cell != "*" else cell for cell in row]))
            
    def place_ships(self, board, num_ships):
        for _ in range(num_ships):
            x = randint(0, self.rows - 1)
            y = randint(0, self.cols - 1)
            while board[x][y] == "@":
                x = randint(0, self.rows - 1)
                y = randint(0, self.cols - 1)
            board[x][y] = "@"

    def valid_guess(self, x, y):
        return (0 <= x < self.rows) and (0 <= y < self.cols) and ((x, y) not in self.previous_guesses)

    def player_turn(self):
        print("Your Turn")
        self.print_boards()
        while True:
            try:
                guess_x = int(input("First row is always 0 - Enter the row: (enter no to start new game): "))

                # Check if the player wants to start new game
                if guess_x == "no":
                    self.reset_game()
                    return

                guess_y = int(input("First column is always 0 - Enter the column: "))

                if not self.valid_guess(guess_x, guess_y):
                    print("Please use number between 3 and 8.")
                else:
                    # Checks current guess and compares it to previous guesses
                    self.previous_guesses.add((guess_x, guess_y))
                    break
            except ValueError:
                print("Please use number between 3 and 8.")

        if self.opponent_board[guess_x][guess_y] == "@":
            print("Player hit a ship!")
            self.opponent_board[guess_x][guess_y] = "*"
            self.player_score += 1
        else:
            print("Player missed.")
            self.opponent_board[guess_x][guess_y] = "X"
            
    def computer_turn(self):
        print("\nComputer Turn")
        computer_guess_x = randint(0, self.rows - 1)
        computer_guess_y = randint(0, self.cols - 1)

        if self.player_board[computer_guess_x][computer_guess_y] == "@":
            print("Computer hit a ship!")
            self.player_board[computer_guess_x][computer_guess_y] = "*"
            self.opponent_score += 1
        else:
            print("Computer missed.")
            self.player_board[computer_guess_x][computer_guess_y] = "X"
