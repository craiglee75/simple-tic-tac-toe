# Tic-Tac-Toe

# prints status of the game
def print_grid():
    print("---------")
    print(f"| {status[0]} {status[1]} {status[2]} |")  # write your code here
    print(f"| {status[3]} {status[4]} {status[5]} |")
    print(f"| {status[6]} {status[7]} {status[8]} |")
    print("---------")

# checks the validity of the player input


def user_move():
    global status
    global move
    global move_index
    move = input(f"Enter the coordinates player {player}: ")

    if move.isalpha():
        print("You should enter numbers!")
        user_move()
    elif " " not in move or int(move[0]) not in range(1, 4) or int(move[2]) not in range(1, 4):
        print("Coordinates should be from 1 to 3!")
        user_move()

    # Check move against grid.  Converts coordinates to the grid index.
    grid = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    x, y = move.split()
    # print(int(x), int(y))
    move_index = grid[int(x)-1][int(y)-1]

    if status[int(move_index)] != " ":
        print("This cell is occupied! Choose another one!")
        user_move()


def change_user():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"


# start of the game
player = "X"
status = "         "
print_grid()

game_status = 1
while game_status == 1:
    user_move()
    new_status = status[:move_index] + player + status[move_index + 1:]
    status = new_status
    print_grid()
    change_user()


# Checks game state to see if anyone has won or played incorrectly
    countxs = status.count("X")
    countos = status.count("O")
    count_s = status.count(" ")
    count_xwin = 0
    count_owin = 0

    # Horizontal wins
    if status[0:3] == "XXX":
        count_xwin += 1
    if status[0:3] == "OOO":
        count_owin += 1
    if status[3:6] == "XXX":
        count_xwin += 1
    if status[3:6] == "OOO":
        count_owin += 1
    if status[6:9] == "XXX":
        count_xwin += 1
    if status[6:9] == "OOO":
        count_owin += 1

    # Diagonal wins
    if status[0] + status[4] + status[8] == "XXX":
        count_xwin += 1
    if status[2] + status[4] + status[6] == "XXX":
        count_xwin += 1
    if status[0] + status[4] + status[8] == "OOO":
        count_owin += 1
    if status[2] + status[4] + status[6] == "OOO":
        count_owin += 1

    # Vertical wins
    if status[0] + status[3] + status[6] == "XXX":
        count_xwin += 1
    if status[1] + status[4] + status[7] == "XXX":
        count_xwin += 1
    if status[2] + status[5] + status[8] == "XXX":
        count_xwin += 1
    if status[0] + status[3] + status[6] == "OOO":
        count_owin += 1
    if status[1] + status[4] + status[7] == "OOO":
        count_owin += 1
    if status[2] + status[5] + status[8] == "OOO":
        count_owin += 1

    # test scenarios and final result
    if abs(countxs - countos) > 1:
        game_status = 0
        print("Impossible")
    elif count_xwin + count_owin == 0 and count_s > 0:
        game_status = 1
        # print("Game not finished")
    elif count_xwin + count_owin == 0 and count_s == 0:
        game_status = 0
        print("Draw")
    elif count_xwin + count_owin > 1 and count_s == 0:
        game_status = 0
        print("Impossible")
    elif count_xwin > 1 or count_owin > 1:
        game_status = 0
        print("Impossible")
    elif count_xwin > 0 and count_owin > 0:
        game_status = 0
        print("Impossible")
    elif count_xwin == 1:
        game_status = 0
        print("X wins")
    elif count_owin == 1:
        print("O wins")
        game_status = 0
