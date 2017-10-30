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

    def move(self,board, start, end, player):
        print()
        for ele in board:
            print(ele)

        print()
        for ele in self.board:
            print(ele)
        print()
        print("___________")
        print(start)
        print()
        print(self.player_1_spaces)
        if player==1:
            self.player_1_spaces.remove(start)
            self.player_1_spaces.append(end)

            if (board[end[0]][end[1]])=="B":
                self.player_2_spaces.remove(end)

            self.board[start[0]][start[1]]="_"
            self.board[end[0]][end[1]]="W"

            if (end in self.player_1_goal_states) or len(self.player_2_spaces)==0:
                self.winner=1

            return self.board

        elif player==2:
            self.player_2_spaces.remove(start)
            self.player_2_spaces.append(end)

            if (board[end[0]][end[1]])=="W":
                self.player_1_spaces.remove(end)

            self.board[start[0]][start[1]]="_"
            self.board[end[0]][end[1]]="B"

            if (end in self.player_2_goal_states) or len(self.player_2_spaces)==0:
                self.winner=2

            return self.board

    def max_value(self,curr_board, player, depth=3):
        if depth==0:
            return (self.get_utility(player), self.board)
        else:
            if player==1:
                mp=self.player_1_movable_pieces
                max_value=-1000000000000000000
                for ele in mp:
                    for it in mp[ele]:
                        new_board=self.move(curr_board, ele, it, 1)
                        for ele in new_board:
                            print(ele)
                        max_value=max(max_value, self.min_value(new_board,2,depth-1))
                    return max_value
            elif player==2:
                mp=self.player_2_movable_pieces
                max_value=-1
                for ele in mp:
                    for it in mp[ele]:
                        new_board=self.move(curr_board,ele, it, 2)
                        max_value=Max(max_value, self.min_value(new_board,1, depth-1))
                    return max_value

    def min_value(self,curr_board, player, depth):
        if depth==0:
            return (self.get_utility(curr_board, player), curr_board)
        else:
            if player==1:
                mp=self.player_1_movable_pieces
                min_val=10000000000000000000
                for ele in mp:
                    for it in mp[ele]:
                        new_board=self.move(curr_board,ele, it, 1)
                        max_value=min(min_value, self.max_value(new_board, 2,depth-1))
                    return max_value
            elif player==2:
                mp=self.player_1_movable_pieces
                min_val=10000000000000000000
                for ele in mp:
                    for it in mp[ele]:
                        print(ele)
                        new_board=self.move(curr_board,ele, it, 2)
                        max_value=min(min_value, self.max_value(new_board, 1,depth-1))
                        return max_value

    def get_utility(self, board, player):
        if player==1:
            val=float(2*len(board.player_2_spaces))+random()
            return val
        elif player==2:
            val=float(2*len(board.player_1_spaces))+random()
            return val














b=breakthrough()
val=b.max_value(b.board,1)
print(val)
'''
temp=""
for ele in b.player_1_movable_pieces:
    temp=ele
    break

b.move(ele,b.player_1_movable_pieces[ele][0], 1)
for ele in b.board:
    print(ele)
'''
