from copy import deepcopy
from random import random

class breakthrough(object):
    def __init__(self,heuristic1=1, heuristic2=2, depth=3):

        self.depth=depth
        self.board=[]
        for ele in range(8):
            thing=[]
            for num in range(8):
                thing.append("_")
            self.board.append(thing)

        self.player_1_spaces=[]
        self.player_2_spaces=[]
        for i in range(0,2):
            for j in range(0,8):
                self.board[i][j]="W"
                self.player_1_spaces.append((i,j))

        for i in range(6,8):
            for j in range(0,8):
                self.board[i][j]="B"
                self.player_2_spaces.append((i,j))


        self.player_1_goal_states=[]
        self.player_2_goal_states=[]

        for i in range(0,1):
            for j in range(0,8):
                self.player_2_goal_states.append((i,j))

        for i in range(7,8):
            for j in range(0,8):
                self.player_1_goal_states.append((i,j))

        self.player_1_movable_pieces=self.movable_pieces(1)
        self.player_2_movable_pieces=self.movable_pieces(2)

        self.p1_heuristic=heuristic1
        self.p2_heuristic=heuristic2

        self.winner=0

    def movable_pieces(self, player):
        movable_pieces={}
        if player==1:
            for ele in self.player_1_spaces:
                adj_spaces=[(ele[0]+1, ele[1]-1),(ele[0]+1, ele[1]), (ele[0]+1, ele[1]+1)]
                ok1_spaces=[]
                for var in adj_spaces:
                    if (var[1]<0 or var[1]>7):
                        pass
                    else:
                        ok1_spaces.append(var)

                ok2_spaces=[]
                for var in ok1_spaces:
                    if (var not in self.player_1_spaces):
                        ok2_spaces.append(var)

                if (len(ok2_spaces)!=0):
                    movable_pieces[ele]=[]
                    for var in ok2_spaces:
                        movable_pieces[ele].append(var)

        elif player==2:
            for ele in self.player_2_spaces:
                adj_spaces=[(ele[0]-1, ele[1]-1),(ele[0]-1, ele[1]), (ele[0]-1, ele[1]+1)]
                ok1_spaces=[]
                for var in adj_spaces:
                    if (var[1]<0 or var[1]>7):
                        pass
                    else:
                        ok1_spaces.append(var)

                ok2_spaces=[]
                for var in ok1_spaces:
                    if (var not in self.player_2_spaces):
                        ok2_spaces.append(var)

                if (len(ok2_spaces)!=0):
                    movable_pieces[ele]=[]
                    for var in ok2_spaces:
                        movable_pieces[ele].append(var)

        return movable_pieces

    def move(self, start, end, player):
        if player==1:
            self.player_1_spaces.remove(start)
            self.player_1_spaces.append(end)

            if(self.board[end[0]][end[1]]=="B"):
                self.board[end[0]][end[1]]="W"
                self.player_2_spaces.remove(end)

            self.player_1_movable_pieces={}
            self.player_2_movable_pieces={}

            self.movable_pieces(1)
            self.movable_pieces(2)

            if ((len(self.player_2_spaces)==0) or (end in self.player_1_goal_states):
                self_winner=1

        elif player==2:
            self.player_2_spaces.remove(start)
            self.player_2_spaces.append(end)

            if(self.board[end[0]][end[1]]=="W"):
                self.board[end[0]][end[1]]="B"
                self.player_1_spaces.remove(end)

            self.player_1_movable_pieces={}
            self.player_2_movable_pieces={}

            self.movable_pieces(1)
            self.movable_pieces(2)

            if ((len(self.player_1_spaces)==0) or (end in self.player_2_goal_states):
                self_winner=2
