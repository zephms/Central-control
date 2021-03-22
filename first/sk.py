import socket
import traceback
import time
import threading
from first.models import Auth

class ClassedPool():
    def __init__(self):
        self.data = {} # 存放 usrName: [sockets...]
    def addWithUsr(usrName, s):
        if Auth.objects.filter(usrName=usrName): # 验证usr是不是账户中的,否则就关闭掉
            maxCount = Auth.objects.filter(usrName=usrName)[0].count  # 该账户的最大值
            curCount = len(self.data.get(usrName, []))
            if maxCount >= curCount:
                if self.data.get(usrName, False):
                    self.data[usrName].append(s)
                else:
                    self.data[usrName] = [s]
        else:
            s.send(bytes("too many users for you", encoding="utf8"))
            s.close()
    def broadcast():
        print("这个东西我懒得写了")
        pass
    def sendCmd(usrName, msg):
        for i in self.data[usrName]:
            try:
                i.send(bytes(msg, encoding="utf8"))
            except Exception as e:
                i.close()
                del i
                print(e)
                continue
    

class Sender1(threading.Thread):
    def __init__(self, address):
        threading.Thread.__init__(self)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind(address)
        self.s.listen(9)
        self.pool = ClassedPool()
        self.start()
    def run(self):
        while True:
            print("waiting...")
            try:
                client_connection, client_address = self.s.accept()
                get = client_connection.recv(300)
                self.pool.addWithUsr(get, client_connection)
            except:
                traceback.print_exc()
                continue
    
    def sendMsg(self, msg):
        for i in self.pool:
            try:
                i.send(bytes(msg, encoding="utf8"))
            except Exception as e:
                del i
                print(e)
                continue


class Sender(threading.Thread):
    def __init__(self, address):
        threading.Thread.__init__(self)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind(address)
        self.s.listen(2)
        self.pool = []
        self.start()
    def run(self):
        while True:
            print("waiting...")
            try:
                client_connection, client_address = self.s.accept()
                self.pool.append(client_connection)
            except:
                traceback.print_exc()
                continue
    
    def sendMsg(self, msg):
        for i in self.pool:
            try:
                i.send(bytes(msg, encoding="utf8"))
            except Exception as e:
                del i
                print(e)
                continue