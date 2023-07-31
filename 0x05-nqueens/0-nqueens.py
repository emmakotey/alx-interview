#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(N, row=0, board=[]):
    if row == N:
        for i in range(N):
            print([i, board[i]])
        return True

    found_solution = False
    for col in range(N):
        if is_safe(board, row, col):
            board.append(col)
            found_solution = solve_nqueens(N, row + 1, board) or found_solution
            board.pop()

    return found_solution


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = []
    if not solve_nqueens(N, 0, board):
        print("No solution found.")
