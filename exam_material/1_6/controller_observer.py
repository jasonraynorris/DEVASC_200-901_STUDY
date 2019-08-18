import socket
from threading import Thread
import json
import hashlib
import uuid

"""reference:https://docs.python.org/3/howto/sockets.html"""

class ControllerObserver:
    def __init__(self, target=None,port=None):
        self.target = target
        self.port = port
        self.sock = self.connect()
        self.out_message_queue = []
        t = Thread(target=self.receive_loop)
        t.start()

    def connect(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.target, self.port))
        return sock

    def disconnect(self):
        self.sock.close()

    def send_message(self,message):
        print(f"Observer Sending Message:{message}")
        self.sock.sendall(bytes(message,"utf-8"))

    def receive_loop(self):
        while True:
            try:
                data = self.sock.recv(1000)
                if not data:
                    break
                print(f"\nObserver Received Message:{data.decode()} ")
            except Exception as ex:
                print(ex)
                break

    def get_serialize(self):
        return self.__dict__

if __name__ == "__main__":
    channel_select = input("join channel A or B?(A/B):")
    """instantiate observer connected to observable"""
    ctl_observer = ControllerObserver(target="192.168.1.37",port=7337)

    """set lengths of fields that are sent first"""
    header_size_field = 8
    header_crc_field = 32

    ###
    """send message to join channel"""
    request_message = {
        "request_id":uuid.uuid4().__str__(),
        "commands":{
                    "join_channel":{
                                    "channel":channel_select,
                                    },
                    }
            }

    message_bytes = str(request_message).encode()
    crc_md5 = hashlib.md5(message_bytes).hexdigest()
    request_message = f"{len(str(request_message)):<{header_size_field}}{crc_md5}" + str(request_message)
    ctl_observer.send_message(request_message)
    """store message and hash for a return?"""
    """"""

    ###
    """send message to channel"""
    request_message = {
        "request_id":uuid.uuid4().__str__(),
        "commands":{
                    "send_channel":{
                                    "channel":channel_select,
                                    "message":"test_message"
                                    },
                    }
            }

    message_bytes = str(request_message).encode()
    crc_md5 = hashlib.md5(message_bytes).hexdigest()
    request_message = f"{len(str(request_message)):<{header_size_field}}{crc_md5}" + str(request_message)
    ctl_observer.send_message(request_message)
    """store message and hash for a return?"""
    """"""

    """"""
    while ctl_observer:
         ctl_observer.send_message(input("\nSend a message:"))


