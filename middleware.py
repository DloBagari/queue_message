#!/usr/bin/python3
#this script must be run in tierminal
#pyton Idle does not support
from collections.abc import Callable
from wsgiref.simple_server import make_server, WSGIServer
from socketserver import ThreadingMixIn
from server import *


class ThreadingWSGIServer(ThreadingMixIn, WSGIServer):
    """"Handler for server to support multithreads, each request to the
    server will run in an independent thread"""
    pass

class MiddleWare(Callable):
    def __init__(self, count):
        #the callback instance to handle the request 
        self.__callback = Server()
        #number of request the server can takes
        self.__count = count

    def __call__(self):
        count = self.__count
        httpd = make_server("",8080, self.__callback, ThreadingWSGIServer)
        if count is None:
            httpd.serve_forever()
        else:
            for c in range(count):
                httpd.handle_request()

if __name__ == "__main__":
    s = MiddleWare(None)
    print("*server is ready*\n")
    s()
    
