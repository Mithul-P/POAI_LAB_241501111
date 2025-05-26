import copy

N = 8

def printSolution(board):
    for row in board:
        for i in range(N):
            print("Q" if row[i] else ".", end=" ")
        print()
    print()

def isSafe(board, row, col):
    for i in range(row):
        if board[i][col]:
            return False
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, N)):
        if board[i][j]:
            return False
    return True

def solve(board, row, solutions, printed):
    if row == N:
        solutions.append(copy.deepcopy(board))
        if not printed[0]:
            printSolution(board)
            printed[0] = True
        return
    for col in range(N):
        if isSafe(board, row, col):
            board[row][col] = 1
            solve(board, row + 1, solutions, printed)
            board[row][col] = 0

def eightQueens():
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    printed = [False]
    solve(board, 0, solutions, printed)
    print(f"Total solutions found: {len(solutions)}")

eightQueens()
