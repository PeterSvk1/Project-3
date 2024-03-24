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
        
