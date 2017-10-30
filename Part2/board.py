from pieces import piece
from players import player
import copy

class board(object):
    def __init__(self):
        self.player_1=player("W")
        self.player_2=player("B")
        self.spaces=[]
        for ele in list(range(8)):
            for num in list(range(8)):
                self.spaces.append((ele,num))
        self.board = [[0 for x in list(range(8))] for x in list(range(8))]
        self.winner=None
        for num in list(range(2)):
            for it in list(range(8)):
                self.board[num][it]=self.player_1.side
                self.board[8-num-1][it]=self.player_2.side

        player_1spaces=[]

        for ele in list(range(2)):
            for num in list(range(8)):
                player_1spaces.append((ele, num))

        player_2spaces=[]
        for ele in list(range(2)):
            for num in list(range(8)):
                player_2spaces.append((8-ele-1, 8-num-1))


        self.player_1.adjust_piece_space(player_1spaces)
        self.player_2.adjust_piece_space(list(reversed(player_2spaces)))

        player_1_goal_states=[64-num-1 for num in list(range(8))]
        player_2_goal_states=[num for num in list(range(8))]

        self.player_1.goal_states=player_1_goal_states
        self.player_2.goal_states=player_2_goal_states

    def get_movable_pieces(self):
        for ele in 




class move(object):
    def __init__(self, source, dest, valid, xs = 0, ys = 0, xd = 0, yd = 0):
        self.source=source
        self.dest=dest
        self.valid=valid
'''
boardA=board()
boardB=copy.deepcopy(boardA)
boardB.board[3][4]="M"
print(boardB.board)
print(boardA.board)
'''

boardA=board()
print(boardA.spaces)
