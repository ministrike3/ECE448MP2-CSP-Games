from pieces import piece

class player(object):
    def __init__(self, side):

        #The side or color of the player
        self.side=side

        #The pieces that the player contains
        self.pieces_array=[]

        #An array of the piece names
        self.piece_val_array=[]

        #The pieces that have been killed
        self.dead_pieces=[]

        #The players winning states on the board
        self.goal_states=[]

        #The players spaces on the board in which any piece cannot move to
        self.occupied_spaces=[]
        for num in list(range(16)):
            temp_piece=piece(side, num)
            self.pieces_array.append(temp_piece)
            self.piece_val_array.append(self.pieces_array[num].val)

    #Initializes the space on the board in which each piece lies
    def adjust_initial_piece_space(self, space):
        for num in list(range(len(self.pieces_array))):
            self.pieces_array[num].adjust_space(space[num])

    # Function that kills the player's pieces
    # removes its position from the occupied space
    # changes the corresponding piece's space to -1
    # puts the name of the piece in the dead pieces
    def kill_piece(self, val):
        for ele in self.pieces_array:
            if ele.val==val:
                self.occupied_spaces.remove(ele.space)
                ele.space=-1
                dead_pieces.append(ele_val)
