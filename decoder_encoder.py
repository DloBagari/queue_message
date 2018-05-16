import time
from message import *
class Decoder_Encoder:
    """encoding and decoding notation , will be used when
    dumping or loading the message instance with json"""
    @staticmethod
    def encoder(object):
        if isinstance(object, Message):
            return dict(
                __class__ = "Message",
                __args__ = [],
                __kw__ = dict(
                    message = object.get_message(),
                    sender = object.get_sender(),
                    rec_date = object.get_rec_date(),
                    receiver = object.get_receiver(),
                    send_date = object.get_send_date()
                    )
                )
        else:
            return json.JSONEncoder.default(o)

    @staticmethod
    def decoder(_json):
        if set(_json.keys()) == {"__class__", "__args__", "__kw__"}:
            class_ = eval(_json["__class__"])
            return class_( *_json["__args__"], **_json["__kw__"])
        else:
            return _json




        
            
