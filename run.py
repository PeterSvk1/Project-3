
# Write your code to expect a terminal of 80 characters wide and 24 rows high


# Beggining of the code for the project 3: BATTLESHIPS project
from random import randint #inport randint so random guesses are working

class BattleshipGame:
    def __init__(self):
        # Welcome message and game information
        print("Welcome to the battleship Game. You will play against the computer. \nAnd here is little more information:\n@ = your ship \n* = destroyed ship \nX = miss \nFirst column and row is always 0")
        print("-------------------------------------------------------------")
        # Initializing game attributes
        self.player_name = ""
        self.rows = 0
        self.cols = 0
        self.player_board = []
        self.opponent_board = []
        self.player_score = 0
        self.opponent_score = 0
        self.previous_guesses = set()
 # Reset all game data       
    def reset_game(self):
        self.player_name = ""
        self.rows = 0
        self.cols = 0
        self.player_board = []
        self.opponent_board = []
        self.player_score = 0
        self.opponent_score = 0
        self.previous_guesses = set()
        self.reset_game_flag = True  # Set the flag to True to indicate game reset
        
 #function to make the board for game
    def create_board(self, rows, cols):
        return [["O" for _ in range(cols)] for _ in range(rows)]
 #function to set up board size according to user input
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
 #set up game its get board size from user input    
    def setup_game(self):
               self.get_board_size()
               self.player_board = self.create_board(self.rows, self.cols)
               self.opponent_board = self.create_board(self.rows, self.cols)
 #print boards for player and computer   
    def print_boards(self):
        print(f"{self.player_name} board:")
        for row in self.player_board:
            print(" ".join(row))
        
        print("Computer:")
        for row in self.opponent_board:
            print(" ".join(["O" if cell != "X" and cell != "*" else cell for cell in row]))
 #places randomly ships on board            
    def place_ships(self, board, num_ships):
        for _ in range(num_ships):
            x = randint(0, self.rows - 1)
            y = randint(0, self.cols - 1)
            while board[x][y] == "@":
                x = randint(0, self.rows - 1)
                y = randint(0, self.cols - 1)
            board[x][y] = "@"
 #function to check if guess is valid and check if it is in the previous guesses
    def valid_guess(self, x, y):
        return (0 <= x < self.rows) and (0 <= y < self.cols) and ((x, y) not in self.previous_guesses)
 #start of player turn function
    def player_turn(self):
        print("Your Turn")
        self.print_boards()
        while True:
            try:
                guess_x = int(input("Enter the row (enter -1 to start new game): "))

                # Check if the player wants to start new game
                if guess_x == -1:
                    self.reset_game()
                    return

                guess_y = int(input("Enter the column: "))

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
 #function for computer turn            
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
            
    def display_scores(self): #displays the scores of the player and the computer
        print(f"\nScores - {self.player_name}: {self.player_score}, Computer: {self.opponent_score}")
        
    def play(self):
        while True:  # Outer loop for replaying the game
            # ask player to put their name
            self.player_name = input("Please enter your name: ")
            print(f"Hello, {self.player_name}! Lets prepare your game!")

            # Set up the game with custom board sizes
            self.setup_game()

            # Place ships on player and computer boards
            num_ships = 3  # number of ships, can be changed
            self.place_ships(self.player_board, num_ships)
            self.place_ships(self.opponent_board, num_ships)

            # Main game loop
            while True:
                self.reset_game_flag = False
                self.player_turn()

                if self.reset_game_flag:
                    break

                # Check if player has won and prints score
                if self.player_score == num_ships:
                    print(f"Congratulations! You won! Your score: {self.player_score}-{self.opponent_score}")
                    break

                self.computer_turn()

                # Check if computer has won and prints score
                if self.opponent_score == num_ships:
                    print(f"Game over! You lost and computer won! Your score: {self.player_score}-{self.opponent_score}")
                    break
            
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != "yes":
                break
            else:
                # Reset all game data if the player wants to play again
                self.reset_game()
                

        print("Thank you for playing Battleship!")
        
# Start the game
game = BattleshipGame()
game.play()
