# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 16:11:43 2019
独学プログラマー15章から
@author: ell_Sub2
"""

#「War Game」
"""
プレイヤーはデッキからカードを引いて、同時に場に出す。
場に出た数字が大きいほうが勝ち。
ヒント:カード、デッキ、プレイヤー、ゲームの要素が必要
"""

from random import shuffle #「randomモジュールから、shuffle()のみインポート」だと思う

class Card:
    suits = ["spades", "hearts", "diamonds", "clubes"] #トランプの4つのマークだ!
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10",
              "Jack", "Qeen", "King", "Ace"] #None2つ = "0"と"1(Ace)"や
    #なぜsuitsとvaluesはタプルじゃないんやろうか。
    def __init__(self, v, s):
        """suit(マーク)も、値も、整数値で渡す"""
        self.value = v
        self.suit = s
    
    def __lt__(self, c2): #self < c2, 「<」の特殊メソッド
        if self.value < c2.value:
            return True
        if self.value == c2.value: #カードの数字が同値なら
            if self.suit < c2.suit: #suit(マーク)で比較する
                return True
            else:
                return False
        return False #c2のが小さければ
    
    def __gt__(self, c2): #self > c2
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                False
        return False
    
    def __repr__(self):
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v
    
#カード一式。has-aの関係で作る。
class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15): #values
            for j in range(4): #suits
                self.cards.append(Card(i, j))
            shuffle(self.cards) #randomモジュールから
    
    def rm_card(self): #リストから要素をpopする
        if len(self.cards) == 0:
            return #Noneを返す
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.card = None
        self.wins = 0 #勝った回数

class Game: #継承してない...てっきり継承するもんかと思ってたけど、それは初学者の考え方なのか。
    def __init__(self):
        self.name1 = input("プレイヤー1の名前を入力してください:")
        self.name2 = input("プレイヤー2の名前を入力してください:")
        self.deck = Deck()
        self.p1 = Player(self.name1)
        self.p2 = Player(self.name2)
        self.rounds = 1
    
    def wins(self, winner):
        w = "ラウンド{}は {} が勝ちまみた。"
        w = w.format(self.rounds, winner)
        print(w)
        self.rounds += 1
        
    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} は {} 、 {} は {} を引きました。"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)
        
    def play_game(self):
        cards = self.deck.cards
        print('...よろしい、ならば戦争"""クリーク"""だ_____。')
        while len(cards) >= 2:
            response = input("qで終了、それ以外のkeyでプレー。")
            if response == 'q':
                break
            
            #カードを引く
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            self.draw(self.p1.name, p1c, self.p2.name, p2c)
            
            #大小判定
            if p1c < p2c:
                self.p2.wins += 1
                self.wins(self.p2.name)
            else:
                self.p1.wins += 1
                self.wins(self.p1.name)
            
        win = self.winner(self.p1, self.p2)
        print("ゲーム終了、{}の勝ちー!".format(win)) #winがNone??
        
    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p2.wins > p1.wins:
            return p2.name
        else:
            return "引き分け"


g = Game()
g.play_game()