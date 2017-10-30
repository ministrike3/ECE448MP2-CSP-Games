from pieces import piece
from players import player
from copy import deepcopy

class board(object):
    def __init__(self):

        # The corresponding players in the board
        self.player_1=player("W")
        self.player_2=player("B")

        #Initializing and emptyy set of spaces on the board
        self.spaces=[]

        #Initializing an empty set of spaces on the board that are occupied
        self.occupied_spaces=[]

        # Appending the boards spaces variable with a tuple in the from of (0,0)----> the tuples go from (0,0) to (7,7)
        for ele in list(range(8)):
            for num in list(range(8)):
                self.spaces.append((ele,num))

        # Pre_populates the board array with a series of zeroes
        self.board = [[0 for x in list(range(8))] for x in list(range(8))]

        #Initializes the boards winner to None because in the beginning there are no zeroes
        self.winner=None



        flipped_player2_pieces=list(reversed(self.player_2.pieces_array))

        #Populates the first two rows of the board with the corresponding pieces of player 1
        for num in list(range(2)):
            for it in list(range(8)):
                self.board[num][it]=self.player_1.pieces_array[(num*8)+it].val

        #Populates the first two rows of the board with the corresponding pieces of player 2
        for num in list(range(6,8)):
            for it in list(range(8)):
                self.board[num][it]=self.player_2.pieces_array[((num-6)*8)+it].val

        player_1spaces=[]

        for ele in list(range(2)):
            for num in list(range(8)):
                player_1spaces.append((ele, num))

        player_2spaces=[]
        for ele in list(range(2)):
            for num in list(range(8)):
                player_2spaces.append((8-ele-1, 8-num-1))

        #initializes the every players piece with their corresponding place on the board
        self.player_1.adjust_initial_piece_space(player_1spaces)
        self.player_2.adjust_initial_piece_space(list(reversed(player_2spaces)))

        #Initializes the spaces on the board in where player 1's pieces cannot move to
        for ele in player_1spaces:
            self.player_1.occupied_spaces.append(ele)

        #Initializes the spaces on the board in where player 2's pieces cannot move to
        for ele in list(reversed(player_2spaces)):
            self.player_2.occupied_spaces.append(ele)

        player_1_goal_states=[64-num-1 for num in list(range(8))]
        player_2_goal_states=[num for num in list(range(8))]

        # Initializes the goal states fo both the players
        self.player_1.goal_states=player_1_goal_states
        self.player_2.goal_states=player_2_goal_states

    #Returns a a dictionary for player 1 where the key is the Piece and the
    #value is a list of tuples where the tuple represents the spaces on the board
    #that each piece can potentially move to
    # dictionary output is in the form {'Piece':[(x,y), (x,y), (x,y)]
    def player1_get_movable_pieces(self):
        movable_pieces={}

        for ele in self.player_1.pieces_array:
            mp=ele.space
            dest_spots=[(int(mp[0])+1,int(mp[1])-1), (int(mp[0])+1,int(mp[1])), (int(mp[0])+1,int(mp[1])+1)]
            allowable_spots=[]
            for spots in dest_spots:
                if (spots[1]<0 or spots[1]>7):
                    x=1
                else:
                    allowable_spots.append(spots)

            non_occupied=[]
            for var in allowable_spots:
                if var in self.player_1.occupied_spaces:
                    x=1
                else:
                    non_occupied.append(var)

            if (len(non_occupied)!=0):
                movable_pieces[ele.val]=non_occupied

        return(movable_pieces)

    #Returns a a dictionary for player 2 where the key is the Piece and the
    #value is a list of tuples where the tuple represents the spaces on the board
    #that each piece can potentially move to
    # dictionary output is in the form {'Piece':[(x,y), (x,y), (x,y)]
    def player2_get_movable_pieces(self):
        movable_pieces={}

        for ele in self.player_2.pieces_array:
            mp=ele.space
            dest_spots=[(int(mp[0])-1,int(mp[1])-1), (int(mp[0])-1,int(mp[1])), (int(mp[0])-1,int(mp[1])+1)]
            allowable_spots=[]
            for spots in dest_spots:
                if (spots[1]<0 or spots[1]>7):
                    x=1
                else:
                    allowable_spots.append(spots)

            non_occupied=[]
            for var in allowable_spots:
                if var in self.player_2.occupied_spaces:
                    x=1
                else:
                    non_occupied.append(var)

            if (len(non_occupied)!=0):
                movable_pieces[ele]=non_occupied

        return(movable_pieces)

    # The position on the board that a player 1's piece can move to
    # it takes in the piece, the pieces starting destination, the pieces
    # ending destination and then it adjusts the pieces position on the board
    # itself. Note that the occupied spaces variable for player 1 is adjusted as well
    def player1_move(self, piece, start, dest):
        piece.space=dest
        self.player_1.occupied_spaces.remove(start)
        self.board[start[0]][start[1]]=0
        self.player_1.occupied_spaces.append(dest)
        self.board[dest[0]][dest[1]]=piece.val


    # The position on the board that a player 2's piece can move to
    # it takes in the piece, the pieces starting destination, the pieces
    # ending destination and then it adjusts the pieces position on the board
    # itself. Note that the occupied spaces variable for player 2 is adjusted as well
    def player2_move(self, piece, start, dest):
        piece.space=dest
        self.player_2.occupied_spaces.remove(start)
        self.board[start[0]][start[1]]=0
        self.player_2.occupied_spaces.append(dest)
        self.board[dest[0]][dest[1]]=piece.val
'''
boardA=board()
boardB=copy.deepcopy(boardA)
boardB.board[3][4]="M"
print(boardB.board)
print(boardA.board)
'''
'''
boardA=board()
for ele in boardA.player_1.pieces_array:
    print(ele.val+ "----"+ str(ele.space))
for ele in boardA.player_2.pieces_array:
    print(ele.val+ "----"+ str(ele.space))
'''

boardA=board()
boardB=deepcopy(boardA)
mp=boardB.player2_get_movable_pieces()
pl=[]
for ele in mp:
    pl.append(ele)
boardB.player2_move(pl[0], pl[0].space, mp[pl[0]][0])
for ele in boardA.board:
    print(ele)
print()
print()
print()
for ele in boardB.board:
    print(ele)
