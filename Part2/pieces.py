class piece(object):
    def __init__(self,side,num):
        self.side=side
        self.number=num
        self.val=self.side+" "+str(self.number)
        self.space=None

    def adjust_space(self, space):
        self.space=space
