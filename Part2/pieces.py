class piece(object):
    def __init__(self,side,num):

        #The Side of each piece
        self.side=side

        #The number of each piece
        self.number=num

        #The value of each piece
        self.val=self.side+""+str(self.number)

        #The space of each piece
        self.space=None

    #Assigns a space on the board to a piece
    def adjust_space(self, space):
        self.space=space
