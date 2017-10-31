import random
import copy

'''
Need to make a board that is 8x8
this board needs to keep track of the positions of each of 16 player on two teams

also need a white player to keep track of their peices
and a black player to keep track of their pieces

just define these by hand

given a player, find the availible moves: ex for white
    take the white players pieces locations  array
    check each of the 3 possible squares to see if the peice can move there
    return a dictionary of possible moves




after define the ability to make a move:

given a board array a start position, and an end position, move the piece to the right place.
return a new board, a new white person list, and a new black player list.
'''
# Player ids: 1 is White, 2 is Black
def setup_game_initial():
    gameboard=[]
    for i in range(0,8):
        newlist=[]
        for j in range (0,8):
            newlist.append('_')
        gameboard.append(newlist)

    initial_black_positions = []
    for i in range(0,2):
        for j in range(0, 8):
            gameboard[i][j]='B'
            initial_black_positions.append((i,j))

    initial_white_positions = []
    for i in range(6,8):
        for j in range(0, 8):
            gameboard[i][j] = 'W'
            initial_white_positions.append((i, j))

    return gameboard,initial_white_positions,initial_black_positions

def find_players_availible_moves(board,piece_positions, player_id):
    moves_dictionary={}
    for position in piece_positions:
        #position is (row, column)
        #white_moves_up,black down
        #white is 1, black is 2
        moves_dictionary[position]=[]

        if player_id==1:
            new_y=position[0]-1
            left_x=position[1]-1
            right_x = position[1] + 1
            if left_x>=0:
                if board[new_y][left_x]!='W':
                    moves_dictionary[position].append((new_y,left_x))

            if board[new_y][position[1]]!='W':
                moves_dictionary[position].append((new_y, int(position[1])))

            if right_x <= 7:
                if board[new_y][right_x]!='W':
                    moves_dictionary[position].append((new_y, right_x))

        if player_id==2:
            new_y = position[0] + 1
            left_x = position[1] - 1
            right_x = position[1] + 1
            if left_x >= 0:
                if board[new_y][left_x] != 'B':
                    moves_dictionary[position].append((new_y, left_x))

            if board[new_y][position[1]] != 'B':
                moves_dictionary[position].append((new_y, int(position[1])))

            if right_x <= 7:
                if board[new_y][right_x] != 'B':
                    moves_dictionary[position].append((new_y, right_x))
    return(moves_dictionary)

def move(gameboard,move_from,move_to,white_positions,black_positions,white_possible_moves,black_possible_moves,player_id):
    #given a board array a start position, and an end position, move the piece to the right place.
    gameboard[move_from[0]][move_from[1]]='_'

    if player_id==1:
        gameboard[move_to[0]][move_to[1]]='W'
        if move_to in black_positions:
            black_positions.pop(move_to)
            black_possible_moves.pop(move_to)
        print(white_positions)
        print(move_from)
        white_positions.remove(move_from)
        white_positions.append(move_to)

    elif player_id==2:
        gameboard[move_to[0]][move_to[1]]='B'
        if move_to in white_positions:
            white_positions.pop(move_to)
            white_possible_moves.pop(move_to)
        black_positions.remove(move_from)
        black_positions.append(move_to)

    return(gameboard,white_positions,black_positions,white_possible_moves,black_possible_moves)

def return_a_duplicate_of_the_playing_feild(gameboard,white_positions,black_positions,white_possible_moves, black_possible_moves):
    new_gameboard=copy.deepcopy(gameboard)
    new_white_positions=copy.deepcopy(white_positions)
    new_black_positions = copy.deepcopy(black_positions)
    new_white_possible_moves=copy.deepcopy(white_possible_moves)
    new_black_possible_moves = copy.deepcopy(black_possible_moves)

    return(new_gameboard,new_white_positions,new_black_positions,new_white_possible_moves,new_black_possible_moves)


def get_utility(other_players_piece_locations):
        return(float(len(other_players_piece_locations)*2)+random())




if __name__ == "__main__":
    gameboard,white_positions,black_positions=setup_game_initial()
    for row in gameboard:
        print(row)
    white_possible_moves = find_players_availible_moves(gameboard,white_positions, 1)
    black_possible_moves = find_players_availible_moves(gameboard, black_positions, 2)
    #gameboard, white_positions, black_positions, white_possible_moves, black_possible_moves = move(gameboard, (6,4), (5,4), white_positions, black_positions, white_possible_moves, black_possible_moves,1)
    new_gameboard, new_white_positions, new_black_positions, new_white_possible_moves, new_black_possible_moves=return_a_duplicate_of_the_playing_feild(gameboard,white_positions,black_positions,white_possible_moves, black_possible_moves)
    new_gameboard, new_white_positions, new_black_positions, new_white_possible_moves, new_black_possible_moves = move(new_gameboard, (6, 1),
                                                                                                   (5, 2),
                                                                                                   new_white_positions,
                                                                                                   new_black_positions,
                                                                                                   new_white_possible_moves,
                                                                                                   new_black_possible_moves,
                                                                                                   1)

    gameboard, white_positions, black_positions, white_possible_moves, black_possible_moves = move(gameboard, (6, 4),
                                                                                                   (5, 4),
                                                                                                   white_positions,
                                                                                                   black_positions,
                                                                                                   white_possible_moves,
                                                                                                   black_possible_moves,
                                                                                                   1)

    for row in gameboard:
        print(row)
    print('\n')
    for row in new_gameboard:
        print(row)

