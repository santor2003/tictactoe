board= [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

user= True

def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot}", end="")
        print()

print_board(board)

def quit(user_input):
    if user_input == "q":
      print("Thanks for playing")  
      return True
    else: return False

def check_input(user_input):
    if not isnum(user_input): return False
    user_input = int(user_input)
    if not bounds(user_input): return False

    return True


def isnum(user_input):
    if not user_input.isnumeric():
        print("This is not a valid number")
        return False
    else: return True

def bounds(user_input):
    if user_input > 9 or user_input < 1:
        print("This number is out of bounds")
        return False
    else: return True

def istaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "-":
        print("This position is already taken")
        return True
    else: return False

    
def coordinates(user_input):
     row = int(user_input / 3)
     col = user_input
     if col > 2: col= int(col % 3)
     return (row,col)

def add_to_board(coords, board, active_user):
    row = coords[0]
    col = coords[1]
    board[row][col] = active_user

def current_user(user):
    if user: return "x"
    else: return "o"

def iswin(user, board):
    if check_row(user, board): return True

def check_row(user, board):
    for row in board:
        complete_row= True
        for slot in row:
            if slot != user:
                complete_row= False
                break
        if complete_row: return True
    return False    

while True:
    active_user= current_user(user)
    user_input= input(" Enter position from 1 through 9 or enter \"q\" to quit:")
    if quit(user_input): break
    if not check_input(user_input):
        print("Please try again.")
        continue
    user_input= int(user_input) - 1
    coords= coordinates(user_input)
    if istaken(coords, board):
        print("Please try again.")
        continue
    add_to_board(coords, board, active_user)
    if iswin(active_user, board):
        print(f"{active_user.upper()} won!")
        break
    
    user= not user


