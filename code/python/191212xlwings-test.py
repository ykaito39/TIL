# -*- coding: utf-8 -*-
import xlwings as xw

KP = "カトウプロ 株式会社"
YMI = "YAMAGATA INTECH 株式会社"
YAM = "YAMAGATA 株式会社"
CMC = "株式会社 シイエム・シイ"
NAS = "那須印刷 株式会社"
CH = "Canada Honda"
CHU = "株式会社 中近東印刷"


# Bmsの情報を格納したDB
# 将来的にフバックエンドからDBを参照することで、日程を一箇所で管理するシステムにする
class BmsDb():
    pass


# OM制作に関わる部分の日程についてのフレームワーク
class Schedule():
    pass


# 車としての情報。
# 将来的には業連等紐付けたい
class Car(Schedule):
    pass

# Omの作り方など
class Om(Schedule):
    part_number = ""
    
    def __init__(self, p_number = "dummy"):
        self.part_number = p_number
    
    def printName(self):
        print(self.part_number)
    
    
# 主言語MLは変わるので毎回入力する
class MainLangOm(Om):
    #基本情報
    #他言語有無、他言語クラスとの関係性など
    #日程
    def __init__(self, p_number):
        pass
    

# 他言語の翻訳編集はMLがほぼ変わらない
class SubLangOm(Om):
    def __init__(self):
        pass


# 発注書
class PurchaseOrder():
    # {言語:["翻訳ML", "編集ML"]}
    # 中近東様は第一のみ入力
    translater_table = {"kc_Fre":[CH, KP], "kd_Cor":[CHU, CHU], 
                        "km_Pol":[None, None], "kk_spa":[YMI, KP,
                        "kx_Spa":[YMI, KP], "ky_Fre":[YMI, KP],
                        "kh_chi":[CHU, CHU]}
    
    def __init__(self):
        
    pass


# スケジュール管理
class ScheduleWindow():
    pass


# 入力される用語の冗長性確保
# 例えばカナ仏とカナダ仏を同じ意味としてもたせるようにする
class RedundantInput():
    pass




#-------------------------------
# test
#-------------------------------
om0 = Om("31TDK610")
om0.printName()

