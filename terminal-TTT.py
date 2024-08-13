def did_user_win(user_set):
    val = False
    for solution in solution_set:
        val = val or (solution<=user_set)
    # print(val)
    return val

def is_game_over():
    if(len(selected_set) == 9):
        print("A DRAW!")
        return True

def print_current_set():
    pattern = [" "," "," "," "," "," "," "," "," ",]
    # pattern = [1,2,3,4,5,6,7,8,9]
    for elements in user_x:
        pattern[elements-1] = "X"
    for elements in user_o:
        pattern[elements-1] = "O"
    print(f"|{pattern[0]}|{pattern[1]}|{pattern[2]}|\n|{pattern[3]}|{pattern[4]}|{pattern[5]}|\n|{pattern[6]}|{pattern[7]}|{pattern[8]}|\n")


print("Tic-Tac-Toe\n")

solution_set = [{1,2,3}, {4,5,6}, {7,8,9}, {1,4,7}, {2,5,8}, {3,6,9}, {1,5,9}, {3,5,7}]

user_x = set()
user_o = set()
selected_set = set()

print(" 1 | 2 | 3")
print(" 4 | 5 | 6")
print(" 7 | 8 | 9\n")

current_user = user_x
user_name = "X"
user_won = did_user_win(current_user)

while(not (is_game_over() or user_won)):
    user_input = int(input(f"choose for player {user_name}: "))
    
    while(user_input<1 or user_input>9):
        print("INVALID INPUT, CHOOSE AGAIN:")
        user_input = int(input(f"choose for player {user_name}: "))
    
    while(user_input in selected_set):
        print("ALREADY TAKEN, CHOOSE AGAIN:")
        user_input = int(input(f"choose for player {user_name}: "))

    current_user.add(user_input)
    selected_set.add(user_input)

    user_won = did_user_win(current_user)

    print_current_set()

    if(user_won):
        print(f"USER {user_name} WON WITH SET {current_user}!")

    if(user_name == "X" and not(user_won)):
        user_name = "O"
        current_user = user_o
    else:
        user_name = "X"
        current_user = user_x
    
    






