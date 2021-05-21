# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 20:37:21 2020

@author: user
"""

import sys
import tkinter as Tk

VERSION = "0.1"

class Application(Tk.Frame):
    def __init__(self, master=None):
        pass
        #Tk.Frame.__init__(self, master) #masterは親widgetを指す
        
        #self.grid()
        
        #widgetを配置する方法:pack, grid, place(widgetのメソッド)
        #  pack:横(縦)一列に並べる
        #  grid:二次元的に配置
        #  place:直接配置
        #Frameにwidgetを配置していく。Frameはwidgetを配置するためのwidget
        #Frameは入れ子にできる
        #一番上のFrameのmainloopメソッドでアプリケーションをつくる
    
    def askfilename(self):
        root = Tk.Tk()
        root.title("DBを開く")
        root.withdraw()
        
        fTyp = [("","*")]
        iDir = os.path.abspath(os.path.dirname(__file__))
        
        path = Tk.filedialog.askopenfilename(filetypes = fTyp, initialdir = iDir)
        
        return path
        
        
        
    
def main():
    #root = Tk.Tk()
    #app = Application(master=root)
    #app.mainloop()
    
    a = Application()
    a.askfilename()
    
if __name__ == "__main__":
    main()