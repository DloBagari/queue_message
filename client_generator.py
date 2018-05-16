from collections.abc import Callable
import threading
from client import *
import time



class ClientGenerator(Callable):
    """return  a client instance when its called by a thread"""
    def __init__(self):
        super().__init__()
        self.__lock = threading.RLock()
        
    def __call__(self, name, host, port):
        with self.__lock:
            return Client(name, host, port)

