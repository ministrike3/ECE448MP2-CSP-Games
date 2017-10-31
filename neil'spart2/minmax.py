from NeilBreakThrough import *

'''
Availible Functions:

gameboard,white_positions,black_positions=setup_game_initial()
Get the start of the game



'''

def min_value(gameboard,white_positions,black_positions,player_id,depth):
    if depth == 0:
        return (get_utility(white_positions, black_positions, player_id))

    else:
        if player_id == 1:

            white_possible_moves = find_players_availible_moves(gameboard, white_positions, 1)
            black_possible_moves = find_players_availible_moves(gameboard, black_positions, 2)

            min_value = 1000000000000000000
            for from_here in white_possible_moves:
                for to_here in white_possible_moves[from_here]:
                    print(from_here)
                    print(to_here)
                    print(white_possible_moves[from_here])

                    new_gameboard, new_white_positions, new_black_positions, new_white_possible_moves, new_black_possible_moves = return_a_duplicate_of_the_playing_feild(
                        gameboard, white_positions, black_positions, white_possible_moves, black_possible_moves)

                    new_gameboard, new_white_positions, new_black_positions, new_white_possible_moves, new_black_possible_moves = move(
                        new_gameboard, from_here, to_here, new_white_positions, new_black_positions,
                        new_white_possible_moves, new_black_possible_moves, 1)

                    max=max_value(new_gameboard, new_white_positions, new_black_positions, 2, depth - 1)

                    min_value = min(min_value,
                                    max_value)

                    return (min_value, from_here, to_here)

        if player_id == 2:

            white_possible_moves = find_players_availible_moves(gameboard, white_positions, 1)
            black_possible_moves = find_players_availible_moves(gameboard, black_positions, 2)

            min_value = 1000000000000000000
            for from_here in black_possible_moves:
                for to_here in black_possible_moves[from_here]:
                    print(from_here)
                    print(to_here)
                    print(black_possible_moves[from_here])
                    new_gameboard, new_white_positions, new_black_positions, new_white_possible_moves, new_black_possible_moves = return_a_duplicate_of_the_playing_feild(
                        gameboard, white_positions, black_positions, white_possible_moves, black_possible_moves)

                    new_gameboard, new_white_positions, new_black_positions, new_white_possible_moves, new_black_possible_moves = move(
                        new_gameboard, from_here, to_here, new_white_positions, new_black_positions,
                        new_white_possible_moves, new_black_possible_moves, 2)

                    min_value = min(min_value,max_value(new_gameboard, new_white_positions, new_black_positions, 1, depth - 1)[0])

                    return (min_value, from_here, to_here)





def max_value(gameboard,white_positions,black_positions,player_id,depth):

    if depth == 0:
        return(get_utility(white_positions,black_positions,player_id))

    else:
        if player_id==1:
            white_possible_moves = find_players_availible_moves(gameboard, white_positions, 1)
            black_possible_moves = find_players_availible_moves(gameboard, black_positions, 2)
            max_value = -1000000000000000000
            for from_here in white_possible_moves:
                for to_here in white_possible_moves[from_here]:
                    print(from_here)
                    print(to_here)
                    print(white_possible_moves[from_here])
                    new_gameboard, new_white_positions, new_black_positions, new_white_possible_moves, new_black_possible_moves = return_a_duplicate_of_the_playing_feild(
                        gameboard, white_positions, black_positions, white_possible_moves, black_possible_moves)

                    new_gameboard, new_white_positions, new_black_positions, new_white_possible_moves, new_black_possible_moves = move(
                        new_gameboard, from_here,to_here,new_white_positions,new_black_positions,new_white_possible_moves,new_black_possible_moves,1)

                    max_value = max(max_value, min_value(new_gameboard,new_white_positions, new_black_positions, 2, depth - 1)[0])

                    return (max_value, from_here, to_here)

        if player_id==2:
            white_possible_moves = find_players_availible_moves(gameboard, white_positions, 1)
            black_possible_moves = find_players_availible_moves(gameboard, black_positions, 2)

            max_value = -1000000000000000000
            for from_here in black_possible_moves:
                for to_here in black_possible_moves[from_here]:
                    print(from_here)
                    print(to_here)
                    print(black_possible_moves[from_here])
                    new_gameboard, new_white_positions, new_black_positions, new_white_possible_moves, new_black_possible_moves = return_a_duplicate_of_the_playing_feild(
                        gameboard, white_positions, black_positions, white_possible_moves, black_possible_moves)

                    new_gameboard, new_white_positions, new_black_positions, new_white_possible_moves, new_black_possible_moves = move(
                        new_gameboard, from_here, to_here, new_white_positions, new_black_positions,
                        new_white_possible_moves, new_black_possible_moves, 2)
                    min=min_value(new_gameboard, new_white_positions, new_black_positions, 1, depth - 1)

                    max_value = max(max_value,
                                    min[0])

                    return(max_value,from_here,to_here)




if __name__ == "__main__":
    gameboard, white_positions, black_positions = setup_game_initial()
    litty=max_value(gameboard, white_positions, black_positions, 1, 3)
    print(litty)

