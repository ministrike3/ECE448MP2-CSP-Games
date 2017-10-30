from tree_gen import Node, minimax
from board import board
import sys

def main():

    game_board=board()
    game_root=Node()
    score=minimax(game_root, game_root.depth, game_root.player)
    print(score)




if __name__=='__main__':
    main()
