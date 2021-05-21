# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:13:02 2019

@author: ell_Sub2
"""

#オセロの反転判断を実装するためのテストコード

"""
pieces = [[],[],[],[],[],[],[],[]]
for line in pieces:
    for i in range(8):
        line.append("□")
このコードは、下のように書ける。
"""

#表示
def print_stage(pieces):
    stage = ""
    for y in range(0, 8):
        for x in range(0, 8):
            stage += pieces[y][x] + ' '
        stage += "\n"
    print(stage)
    
#新しく置いたコマから見て左側の同色コマまでを反転する
#今回は抽象化せず、黒で挟んで白を反転させることに限定する。
def reverse_row_left(pieces_row, x_offset): #x_offsetは新しく置いたコマの位置
    change_rocation_x = x_offset
    for x in range(x_offset-1, 0, -1):
        if (pieces_row[x] == "○"):
            continue #白が途切れて、途切れた次が"●"なら、その場所の座標を記録したい
        if (pieces_row[x] == "●") and (x is not x_offset):
            change_rocation_x = x
            break
        else:
            return pieces_row
    
    for x in range(x_offset, change_rocation_x, -1):
        pieces_row[x] = "●"
    
    return pieces_row


def reverse_row(pieces_row, x_offset): #x_offsetは新しく置いたコマの位置
    #コマを置いた左側
    target_x_left = x_offset
    for x_left in range(x_offset-1, -1, -1):
        if (pieces_row[x_left] == "○"):
            continue
        if (pieces_row[x_left] == "●") and (x_left is not x_offset):
            target_x_left = x_left
            break
        else:
            break
    
    #コマを置いた右側
    target_x_right = x_offset
    for x_right in range(x_offset+1, 8):
        if (pieces_row[x_right] == "○"):
            continue
        if (pieces_row[x_right] == "●") and (x_right is not x_offset):
            target_x_right = x_right
            break
        else:
            break
 
    #書き換え
    for x in range(x_offset, target_x_left, -1):
        pieces_row[x] = "●"
        
    for x in range(x_offset, target_x_right):
        pieces_row[x] = "●"
    
    return pieces_row

#注意:is演算子はIDの同一性を確認する



#置く+上下左右の対象を反転
def put_and_reverse(pieces, x_offset, y_offset): #x_offsetは新しく置いたコマの位置
    pieces[y_offset][x_offset] = "●"
    ########################################
    #行
    ########################################
    
    #コマを置いた左側
    target_x_left = x_offset
    for x_left in range(x_offset-1, -1, -1):
        if (pieces[y_offset][x_left] == "○"):
            continue
        if (pieces[y_offset][x_left] == "●") and (x_left is not x_offset):
            target_x_left = x_left
            break
        else:
            break
    
    #コマを置いた右側
    target_x_right = x_offset
    for x_right in range(x_offset+1, 8):
        if (pieces[y_offset][x_right] == "○"):
            continue
        if (pieces[y_offset][x_right] == "●") and (x_right is not x_offset):
            target_x_right = x_right
            break
        else:
            break
 
    #書き換え
    for x in range(x_offset, target_x_left, -1):
        pieces[y_offset][x] = "●"
        
    for x in range(x_offset, target_x_right):
        pieces[y_offset][x] = "●"
        
    
    ########################################
    #列
    ########################################
    #コマを置いた上側
    target_y_upper = y_offset
    for y_upper in range(y_offset-1, -1, -1):
        if (pieces[y_upper][x_offset] == "○"):
            continue
        if (pieces[y_upper][x_offset] == "●") and (y_upper is not y_offset):
            target_y_upper = y_upper
            break
        else:
            break
    
    #コマを置いた下側
    target_y_lower = y_offset
    for y_lower in range(y_offset+1, 8):
        if (pieces[y_lower][x_offset] == "○"):
            continue
        if (pieces[y_lower][x_offset] == "●") and (y_lower is not y_offset):
            target_y_lower = y_lower
            break
        else:
            break
 
    #書き換え
    for y in range(y_offset, target_y_upper, -1):
        pieces[y][x_offset] = "●"
        
    for y in range(y_offset, target_y_lower):
        pieces[y][x_offset] = "●"    
    
    return pieces



#[注]pieces = [["・"] * 8]*8だと、内部のリストオブジェクトは全部同一IDになってしまう。
pieces = [["□" for x in range(8)] for y in range(8)] #正しい書き方

"""
#横に並べた白を、黒が挟んでひっくり返せそうな状態を作ってみる
pieces[4][0] = "●"
for x in range(1, 3):
    pieces[4][x] = "○"

pieces[4][7] = "●"
for x in range(4, 7):
    pieces[4][x] = "○"
print_stage(pieces)

#挟んでみる
X = 3
pieces[4][X] = "●"
print_stage(pieces)

pieces[4] = reverse_row(pieces[4], X)
print_stage(pieces)
"""
pieces[3][3] = "●"
pieces[3][4] = "○"
pieces[4][3] = "○"
pieces[4][4] = "●"
print_stage(pieces)

pieces = put_and_reverse(pieces, 4, 2)
#print(pieces)

print_stage(pieces)