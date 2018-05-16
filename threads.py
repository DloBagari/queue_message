#!/usr/bin/python3
#this script must be run in tierminal
#pyton Idle does not support multithreads

import concurrent.futures
import time
import threading
from middleware import *
from client_generator import *


class MyThread(threading.Thread):
    """create a thread for a client"""
    def __init__(self, name, message=None, host="localhost", port=8080):
        super().__init__()
        self.name = name
        self.message = message
        self.host_server = host
        self.port_server = port

    #Override the run method 
    def run(self):
        lock.acquire()
        current = threading.current_thread().name
        print("Currently running thread is thread for %s" %(self.name),
              file=sys.stderr)
        client = get_client(self.name,self.host_server, self.port_server)
        if self.message is None:
            client.getitem()
        else:
            client.setitem(self.message)
        lock.release()




    






   
get_client = ClientGenerator()   
lock = threading.Lock()         
if __name__ == "__main__":
    t1 = MyThread("Client_1","submit by Client_1")
    t2 = MyThread("Client_2")
    t3 = MyThread("Client_3")
    t4 = MyThread("Client_4","submit by Client_4")
    t6 = MyThread("Client_6","submit by Client_6")
    t7 = MyThread("Client_7")
    t8 = MyThread("Client_8")
    t9 = MyThread("Client_9","submit by Client_9")
    t10 = MyThread("Client_10","submit by Client_10")
    t11 = MyThread("Client_11","submit by Client_11")
    t12 = MyThread("Client_12","submit by Client_12")
    t13 = MyThread("Client_13")
    t14 = MyThread("Client_14")
    threads = [t1,t2,t3,t4,t6,t7,t8,t9,t10, t11, t12, t13 ,t14]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        print("*Running the Server..*")
        #executor.submit(MiddleWare(8))
        #time.sleep(1)
        #print("*Server is Ready*\n")
        #time.sleep(2)
        for thread in threads:
            executor.submit(thread.start())
            
            
        


   
