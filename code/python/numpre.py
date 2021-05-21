# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 22:23:28 2020

@author: user
"""

class Game():
    def __init__(self, board):
        self.board = board
        self.result = []
    
    def start(self):
        self.result = self.board.corrected()
        print(result)
        


"""
3x3に分割
"""
class SmallBoard():
    def __init__(self, small_board):
        self.small_board #2次元配列で与える
    
    #回答を返す
    def corrected(self):
        pass

"""
行で分割
"""
class Row():
    pass

"""
列で分割
"""
class Column():
    pass


"""
ゲーム全体のボード(9x9)
Gmaeクラスに与える
"""
class Board():
    def __init__(self, board):
        self.cols = [col for col in board]
        self.rows = [board[i] for i in range(len(board[0]))]
        self.small_boards = [small_board for small_board in small_boards]
    
    def corrected(self):
        results = [b.correced for b in small_boards]
        return result
        
#http://www.sudokugame.org/archive/printsudoku.php?nd=0&xh=1
test_board = [[None, None, None, None, None, None, None, None, None],
              [None, None, None, None, None, None, None, 2,    7   ],
              [4,    None, None, 6   , None, 8   , None, None, None],
              [None, 7   , 1   , None, None, None, 3   , None, None],
              [2   , 3   , 8   , 5   , None, 6   , 4   , 1   , 9   ],
              [9   , 6   , 4   , 1   , None, None, 7   , 5   , None],
              [3   , 9   , 5   , None, 2   , 7   , 8   , None, None],
              [1   , 8   , 2   , None, 6   , None, 9   , 7   , 4   ],
              [None, 4   , 6   , 8   , 1   , 9   , 2   , None, 5   ]]

g = Gmae(test_board)
g.start