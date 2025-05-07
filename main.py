import os

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # 3x3 board represented as a list
        self.current_winner = None  # Keep track of the winner

    def print_board(self):
        """Prints the game board in a 3x3 grid."""
        for i in range(3):
            print("| " + " | ".join(self.board[i*3:(i+1)*3]) + " |")
            if i < 2:
                print("---------")

    @staticmethod
    def print_board_nums():
        """Prints the numbers for user reference."""
        number_board = [[str(i) for i in range(1 + x*3, 4 + x*3)] for x in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")
            if row != number_board[-1]:
                print("---------")

    def available_moves(self):
        """Returns a list of indices that are empty on the board."""
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def empty_squares(self):
        """Returns a boolean if there are empty spots on the board."""
        return " " in self.board

    def winner(self, square, letter):
        """Checks if a player has won."""
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
            [0, 4, 8], [2, 4, 6]               # diagonal
        ]
        for condition in win_conditions:
            if all(self.board[i] == letter for i in condition):
                return True
        return False

    def play(self, player, square):
        """Plays a move on the board."""
        if self.board[square] == " ":
            self.board[square] = player
            if self.winner(square, player):
                self.current_winner = player
            return True
        return False

def play_game():
    game = TicTacToe()
    player = "X"

    print("Welcome to Tic Tac Toe!")
    game.print_board_nums()

    while game.empty_squares():
        if player == "O":
            square = int(input(f"{player}'s turn. Enter a move (1-9): ")) - 1
        else:
            square = int(input(f"{player}'s turn. Enter a move (1-9): ")) - 1

        if game.play(player, square):
            game.print_board()
            if game.current_winner:
                print(f"{player} wins!")
                break
            player = "O" if player == "X" else "X"
        else:
            print("Invalid move. Try again.")

    if not game.current_winner:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()
