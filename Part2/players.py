from pieces import piece

class player(object):
    def __init__(self, side):

        #The side or color of the player
        self.side=side

        #The pieces that the player contains
        self.pieces_array=[]

        #The pieces that have been killed
        self.dead_pieces=[]

        #The players winning states on the board
        self.goal_states=[]

        #The players spaces on the board in which any piece cannot move to
        self.occupied_spaces=[]
        for num in list(range(16)):
            temp_piece=piece(side, num)
            self.pieces_array.append(temp_piece)
            #print(self.pieces_array[num].val)

    #Initializes the space on the board in which each piece lies
    def adjust_initial_piece_space(self, space):
        for num in list(range(len(self.pieces_array))):
            self.pieces_array[num].adjust_space(space[num])

'''
player_1=player("W")
for ele in player_1.pieces_array:
    print(ele.val)
'''
