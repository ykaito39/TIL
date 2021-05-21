# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 21:12:23 2019
独学プログラマー10章 ハングマン
@author: ell_Sub2
"""
import random

def hangman(word):
    wrong = 0 #多分ミスった回数だな
    stages = ['',
              '______        ',
              '|             ',
              '|     |       ',
              '|     o       ',
              '|   / | \     ',
              '|    / \      ',
              '|             ']
    rletters = list(word) #wordを一単語ごとに区切ってList化。
                          #答えるべき残りの文字を覚えておくため。文字列はイミュータブルだからね。
    board = ['_'] * len(word)
    win = False
    print('ハングマンへようこそ!')

    #Game main
    while wrong < len(stages) -1:
        print('\n')
        
        msg = '一文字入力してね'
        char = input(msg)
        if char in rletters: #index()を使うには文字が含まれるか確認したいため
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        
        #スコアボードの表示
        print(' '.join(board))
        
        #hungmanの表示
        e = wrong + 1 #ターン数か?
        print('\n'.join(stages[0:e]))
        
        #プレイヤー2が勝ったかどうか
        if '_' not in board:
            print('YOU WIN')
            print(' '.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0:wrong+1]))
        print('YOU LOSE. 正解は{}'.format(word))
            
correcters = ['dog', 'cat', 'milktea', 'lion']
hangman(correcters[random.randint(0, len(correcters))]) #可読性がクソい