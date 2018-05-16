from collections.abc import Callable
import wsgiref.util
import json
import threading
from queue_message import *
from message import *
from decoder_encoder import *


class Server (Callable):
    """ callback class to handle the submitted requests"""
    def __init__(self):
        self.queue = Queue()
    def __call__(self, environ, start_response):
        lock.acquire()
        #get the client name from request environment
        client = wsgiref.util.shift_path_info(environ)
        try:
            method = environ["REQUEST_METHOD"]
            if method == "GET":

                
                status = "200 OK"
                headers = [("Content-Type", "application/json; charset=utf-8")]
                if not self.queue.has_next():
                    status = "401 NO_MESSAGES_AVAILABLE"
                    document = json.dumps("{0}: NO_MESSAGES_AVAILABLE".format(client))
                else:
                    message_to_send = self.queue.next_message()
                    message_to_send.set_receiver(client)
                    document = json.dumps(message_to_send, default=Decoder_Encoder.encoder)
                                        
                start_response(status, headers)
                return [document.encode("UTF-8")]
            elif method == "POST":
                try:
                    length= int(environ.get('CONTENT_LENGTH', '0'))
                except ValueError:
                    length= 0
                if length !=0:
                    
                    _json = environ['wsgi.input'].read(length).decode("UTF-8")
                    message = json.loads(_json, object_hook=Decoder_Encoder.decoder)
                    self.queue.append(message)
                    #assert self.q.size() != 0
                    status = "200 OK"
                    headers = [("Content-Type", "application/json; charset=utf-8")]
                    start_response(status, headers)
                    return [json.dumps("{0} add a message to the Queue at {1}".\
                                       format(message.get_sender(),
                                              message.get_rec_date())).encode("UTF-8")]
                else:
                    status = "403 FORBIDDEN"
                    headers = [("Content-Type", "application/json; charset=utf-8")]
                    start_response(status, headers)
                    return [json.dumps("Error: 403 FORBIDDEN no data Attached").encode("UTF-8")]
                    
                    
            else:
                status = "405 METHOD_NOT_ALLOWED"
                headers = [("Content-Type", "application/json; charset=utf-8")]
                start_response(status, headers)
                return [json.dumps("Error: 405 METHOD_NOT_ALLOWED").encode("UTF-8")]
        finally:

            lock.release()
            #pass
          
 # the locker instance               
lock = threading.Lock()


            

