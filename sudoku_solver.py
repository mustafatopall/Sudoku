# Sudoku tahtası (0 olan yerler boş)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if board[i][j] == 0:
                print(".", end=" ")
            else:
                print(board[i][j], end=" ")
        print()

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, num, pos):
    row, col = pos

    for i in range(len(board[0])):
        if board[row][i] == num and col != i:
            return False

    for i in range(len(board)):
        if board[i][col] == num and row != i:
            return False

    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(board):
    empty = find_empty(board)
    if not empty:
        return True  # Çözüm bulundu
    row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False

# Sudoku çözücüyü çalıştır
print("Başlangıç Sudoku Tahtası:\n")
print_board(board)

if solve(board):
    print("\nÇözülmüş Sudoku Tahtası:\n")
    print_board(board)
else:
    print("\nÇözüm bulunamadı.")
