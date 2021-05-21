# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 00:01:42 2020

@author: ell
"""


from socket import socket, AF_INET, SOCK_STREAM
from multiprocessing import Process
import time

HOST = "localhost"
PORT = 52000
MAX_MESSAGE = 2048
NUM_THREAD = 4

#receiveに定期的に信号を送るも(queueが溜まってたら実行するため)
def interval_signal(sec): #多分動いていない
    try:        
        while True:
            sock = socket(AF_INET, SOCK_STREAM)
            sock.connect((HOST, PORT))
            sock.send("interval".encode("utf-8"))
            time.sleep(sec)
            sock.close()
        
    except Exception as e:
        print(str(e))

#受信メッセージ(コマンド)のキュー
class Queue():
    def __init__(self):
        self.l = []
    
    def pop(self):
        if len(self.l) == 0:
            return None
        
        return self.l.pop(0)
    
    def push(self, value):
        self.l.append(value)
    
    def __len__(self):
        return len(self.l)
        
def com_receive():
    q = Queue() #queue
    
    #通信の確立
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(NUM_THREAD)
    
    print("ready. ")
    
    #メッセージを受信
    while True:
        try:
            conn, adder = sock.accept()
            message = conn.recv(MAX_MESSAGE).decode("utf-8")
            conn.close()
            
            #intervalを受信した場合はqueueから一つ摂ってきてプログラムを実行
            if message == "interval":
                print(q.pop())
                #ここでサブプロセスが終わったか確認する
                    #終わっている場合だけqueueから一つ摂ってきて実行
            else:
                q.push(message)
                
            #if len(q) >= 3: #擬似的に、qが３つ溜まってたら出力するようにする
            #    for i in range(3):
            #        print(q.pop())
            #else:
            #    print("queue is less than 3 items.")
            #受信はできるけど、processingしたサブプロセスの終了状態を取得できない。
            #取得するには、タイマでsocketを送るプログラムが必要?
        except Exception as e:
            print(str(e))
    
    sock.close()
    print("connection finish.")

def proc():
    com_receive()
    
    
if __name__ == "__main__":
    process = Process(target=interval_signal, kwargs={"sec":3})
    process.start()
    proc()