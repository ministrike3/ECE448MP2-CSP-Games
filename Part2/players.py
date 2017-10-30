from pieces import piece

class player(object):
    def __init__(self, side):
        self.side=side
        self.pieces_array=[]
        self.dead_pieces=[]
        self.goal_states=[]
        for num in list(range(16)):
            temp_piece=piece(side, num)
            self.pieces_array.append(temp_piece)

    def adjust_piece_space(self, space):
        for num in list(range(len(self.pieces_array))):
            self.pieces_array[num].adjust_space(space[num])

    
