from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        rows = [self.board[i*3:(i+1)*3] for i in range(3)]
        return rows

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' ']

    def play(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.check_winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def check_winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        col = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

@app.route("/")
def home():
    game = TicTacToe()
    return render_template("index.html", board=game.print_board(), winner=None)

@app.route("/play", methods=["POST"])
def play():
    square = int(request.form.get("square"))
    letter = request.form.get("letter")
    game = TicTacToe()
    game.play(square, letter)
    winner = game.current_winner
    return render_template("index.html", board=game.print_board(), winner=winner)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
