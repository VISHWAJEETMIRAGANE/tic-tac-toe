from flask import Flask, render_template, request
import os

app = Flask(__name__)

class TicTacToeGame:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def get_board(self):
        return self.board

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for a, b, c in winning_combinations:
            if self.board[a] == self.board[b] == self.board[c] != ' ':
                return self.board[a]
        if ' ' not in self.board:
            return 'Draw'
        return None

    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

game = TicTacToeGame()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        move = request.form.get('move')
        if move and move.isdigit():
            move = int(move) - 1
            game.make_move(move)

    winner = game.check_winner()
    board = game.get_board()

    return render_template('index.html', board=board, winner=winner)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8081))
    app.run(debug=True, host='0.0.0.0', port=port)
