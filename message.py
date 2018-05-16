import time
class Message:
    "create an message instance "

    def __init__(self, message, sender,rec_date=time.asctime(),
                 receiver=None, send_date=None):
        self.__message = message
        self.__sender = sender
        self.__receiver = receiver
        self.__rec_date = rec_date
        self.__send_date = send_date

    def set_receiver(self, receiver):
        self.__receiver = receiver

            
    def get_message(self):
            return self.__message

    def get_sender(self):
        return self.__sender

    def get_send_date(self):
        return self.__send_date

    def get_rec_date(self):
        return self.__rec_date

    def get_receiver(self):
        return self.__receiver
    
