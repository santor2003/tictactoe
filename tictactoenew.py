board= [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot}", end="")
        print()

print_board(board)

while True:
    user_input= input(" Enter position from 1 through 9")