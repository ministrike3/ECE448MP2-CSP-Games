from board import board
from copy import deepcopy, copy
from anytree import Node, RenderTree
from sys import maxsize
import sys
from random import random
sys.setrecursionlimit(1500)
class Node(object):
    def __init__(self, player=1,depth=2,board=board(), value=0):
        self.depth=depth
        self.board=board
        self.player=player
        self.value=self.heuristic_1score(board, 1)
        self.children=[]
        self.createChildren()

    #Function to create the chldren
    def createChildren(self):
        if self.depth>=0:
            for i in list(range(1,4)):
                if (self.player==1):
                    #gets the dictionary
                    mp=self.board.player1_get_movable_pieces()

                    #gets the pieces
                    pl=[]
                    for ele in mp:
                        pl.append(ele)

                    #Creates a list a adjusted boards
                    adj_board=[]

                    # Creates the children by moving the pieces on the board
                    for num in list(range(len(mp))):
                        for it in list(range(len(mp[pl[num]]))):
                            new_board=deepcopy(self.board)
                            curr_piece=new_board.player_1.get_piece(pl[num])
                            new_board.player1_move(curr_piece, curr_piece.space, mp[pl[num]][it])
                            adj_board.append(new_board)

                    #Creating empty child nodes
                    for num in list(range(len(adj_board))):
                        print(str(num))
                        temp_node=Node(2, self.depth-1, adj_board[num], self.heuristic_1score(adj_board[num], 2))
                        self.children.append(temp_node)

                elif(self.player==2):
                    #gets the dictionary
                    mp=self.board.player2_get_movable_pieces()

                    #gets the pieces
                    pl=[]
                    for ele in mp:
                        pl.append(ele)

                    #Creates a list a adjusted boards
                    adj_board=[]

                    # Creates the children by moving the pieces on the board
                    for num in list(range(len(mp))):
                        for it in list(range(len(mp[pl[num]]))):
                            new_board=deepcopy(self.board)
                            curr_piece=new_board.player_2.get_piece(pl[num])
                            new_board.player2_move(curr_piece, curr_piece.space, mp[pl[num]][it])
                            adj_board.append(new_board)

                    #Creating empty child nodes
                    for num in list(range(len(adj_board))):
                        print(str(num))
                        temp_node=Node(1, self.depth-1, adj_board[num], self.heuristic_1score(adj_board[num],1))
                        self.children.append(temp_node)


    #function to get the heuristic scores
    def heuristic_1score(self, board, player):
        if (player==1):
            p2_pieces=len(board.player_2.occupied_spaces)
            score=float(2*p2_pieces)+random()
            return score
        elif(player==2):
            p1_pieces=len(board.player_1.occupied_spaces)
            score=float(2*p1_pieces)+random()
            return score
        return 0

##==========================================================================
#Algorithm

#function for the minimax pruning
def minimax(node, depth, player):
    if ((depth==0) or (node.board.winner==1 and player==1) or (node.board.winner==2 and player==2)):
        return (node.value)

    best_score=node.heuristic_1score(node.board, player)

    for i in list(range(len(node.children))):
        child=node.children[i]
        score=0
        if (player==1):
            score=minimax(child,depth-1,2)
        elif(player==2):
            score=minimax(child,depth-1,1)

        if (score<best_score):
            score=best_score

        print(str(depth)+"--"+str(score))

    return best_score
