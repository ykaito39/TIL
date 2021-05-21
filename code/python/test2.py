# -*- coding: utf-8 -*-
board = []
board.append("・・・・・・・・")
board = board * 8

raw_row = board[4-1]

mae = raw_row[:(4-1)]
ushiro = raw_row[4:-1]

tmp_row = mae + "○" + ushiro
board[4-1] = tmp_row #うまくいかん...

print(board)