import http.client
import json
import sys
from message import *
from decoder_encoder import *


class Client :
    """create a client instance , each client can send a request to get
    a message or to set a message"""
    def __init__(self, name, host, port):
        self.name = name
        #RestFul http connection
        self.rest = http.client.HTTPConnection(host, port)

    def setitem(self, message):
        """send the message to the Middleware to be handled"""
        object = json.dumps(Message(message, self.name),indent=4,
                                          default=Decoder_Encoder.encoder)
        self.rest.request("POST","/", body=object)
        response = self.rest.getresponse()
        row = response.read().decode("UTF-8")
        if response.status == 200:
            print(json.loads(row),"\n")
        else:
            print(json.loads(row) + "\n", file=sys.stderr)


    def getitem(self):
        """send a request asking for a message"""
        self.rest.request("GET","/"+self.name)
        response = self.rest.getresponse()
        _json = response.read().decode("UTF-8")
        if response.status == 200:
            message = json.loads(_json, object_hook=Decoder_Encoder.decoder)
            print("{0} got a message form the Queue sent by {1} at {2}\n".
                  format(message.get_receiver(), message.get_sender(),
                         message.get_rec_date()))
            
        else:
            print(json.loads(_json) + "\n", file=sys.stderr)
