import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to represent the 3x3 board
        self.current_winner = None  # Keep track of the winner!

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # If valid move, then make the move (assign square to letter)
        # Then return true. If invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Winner if 3 in a row anywhere. We have to check all of these!
        # First let's check the row
        row_ind = square // 3
        row = self.board[row_ind * 3:(row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        # Check column
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        # Check diagonals
        # Only if the square is an even number (0, 2, 4, 6, 8)
        # These are the only moves possible to win a diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        # If all checks fail
        return False

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.game = TicTacToe()
        self.current_player = 'X'

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, text=' ', font=('Arial', 20), width=4, height=2,
                                   command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)

        self.status_label = tk.Label(self.root, text="Player X's turn", font=('Arial', 16))
        self.status_label.grid(row=3, columnspan=3)

    def make_move(self, i, j):
        if self.game.board[i * 3 + j] == ' ' and not self.game.current_winner:
            self.game.make_move(i * 3 + j, self.current_player)
            self.buttons[i][j].config(text=self.current_player)
            if self.game.current_winner:
                self.display_winner()
            elif not self.game.empty_squares():
                self.display_tie()
            else:
                self.switch_player()

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.status_label.config(text=f"Player {self.current_player}'s turn")

    def display_winner(self):
        winner = self.game.current_winner
        messagebox.showinfo("Game Over", f"Player {winner} wins!")
        self.reset_board()

    def display_tie(self):
        messagebox.showinfo("Game Over", "It's a tie!")
        self.reset_board()

    def reset_board(self):
        self.game = TicTacToe()
        self.current_player = 'X'
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=' ')
        self.status_label.config(text="Player X's turn")

if __name__ == '__main__':
    root = tk.Tk()
    tic_tac_toe_gui = TicTacToeGUI(root)
    root.mainloop()
