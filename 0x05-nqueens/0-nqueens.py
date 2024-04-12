#!/usr/bin/python3
import sys


def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at position (row, col) on the board."""
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, row, n, solutions):
    """Recursive function to solve the N Queens problem."""
    if row == n:
        solutions.append([(i, col) for i, col in enumerate(board[row - 1])])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens_util(board, row + 1, n, solutions)
            board[row][col] = 0


def print_solution(solution):
    """Print the N Queens solution in the specified format."""
    for row, col in solution:
        print("[{}, {}]".format(row, col), end=" ")
    print()


def solve_n_queens(n):
    """Solve the N Queens problem and print solutions."""
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    for solution in solutions:
        print_solution(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    solve_n_queens(sys.argv[1])
