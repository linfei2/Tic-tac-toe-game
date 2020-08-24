game = [
    [0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]
]

ask_p1 = 'Player 1, where do you want to place X?' '\n' \
'Enter coordinates in (row,column) format '  \
'or type q to quit: '
ask_p2 = 'Player 2, where do you want to place @?' '\n' \
'Enter coordinates in (row,column) format ' \
'or type q to quit: '
win1 = 'Player 1 wins!'
win2 = 'Player 2 wins!'
no_winner = 'No winner this time.'
error = 'Invalid format. Try again.'
taken = 'This place is taken. Enter other coordinates.'

def show_board():
    print()
    for sublist in game:
        print(*sublist)
    print()


def find_winner(g_array):
    # Checking rows
    for sublist in g_array:             
        if sublist == ['X', 'X', 'X']:
            return win1
        elif sublist == ['@', '@', '@']:
            return win2
    # Checking columns
    for c in list(zip(*g_array)):    
        if c == ('X', 'X', 'X'):
            return win1
        elif c == ('@', '@', '@'):
            return win2
    # Checking diagonals
    if (
        g_array[0][0]=='X' and g_array[1][1]=='X' and g_array[2][2]=='X'
        or g_array[0][2]=='X' and g_array[1][1]=='X' and g_array[2][0]=='X'):
            return win1
    elif (
        g_array[0][0]=='@' and g_array[1][1]=='@' and g_array[2][2]=='@'
        or g_array[0][2]=='@' and g_array[1][1]=='@' and g_array[2][0]=='@'):
            return win2


def p1_turn():
    while True:
        p1_input = input(ask_p1)
        if p1_input != 'q':
        # Checking format
            try:
                row, col = p1_input.split(',')
                p1_row = int(row)
                p1_col = int(col)
            except (ValueError, IndexError):
                print('\n', error)
                show_board() 
                continue
            # Assigning value if given place is free
            if game[p1_row-1][p1_col-1] == 0:
                game[p1_row-1][p1_col-1] = 'X'
                show_board()
                # Checking for winner
                find_winner(game)
                if find_winner(game)==win1 or find_winner(game)==win2:
                    print(find_winner(game))
                    break
                # Checking for free places left
                elif not any(0 in sublist for sublist in game):
                    print('\n', no_winner, '\n')
                    break
                # Moving to Player 2
                else:
                    p2_turn()
                    break
            # Displaying message if given place is taken     
            else:
                print('\n', taken)
                show_board()
                continue
        else:
            break

def p2_turn():
    while True:
        p2_input = input(ask_p2)
        if p2_input != 'q':
            try:
                row, col = p2_input.split(',')
                p2_row = int(row)
                p2_col = int(col)
            except (ValueError, IndexError):
                print('\n', error)
                show_board()
                continue
            if game[p2_row-1][p2_col-1] == 0:
                game[p2_row-1][p2_col-1] = '@'
                show_board()
                find_winner(game)
                if find_winner(game)==win1 or find_winner(game)==win2:
                    print(find_winner(game))
                    break
                elif not any(0 in sublist for sublist in game):
                    print('\n', no_winner, '\n')
                    break
                else:
                    p1_turn()
                    break
            else:
                print('\n', taken)
                show_board()
                continue
        else:
            break

show_board()
p1_turn()