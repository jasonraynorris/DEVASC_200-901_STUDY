import socket
from threading import Thread
import json
import hashlib

class CommunicationHandler(object):
    def __init__(self, hosting_if_ip, port):
        self.message_listeners = []
        """setup listener"""
        sock = self.sock_listen(hosting_if_ip, port)
        while True:
            """accept connection attempts"""
            self.sock_message_handler(sock)

    def sock_listen(self,hosting_if_ip,port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((hosting_if_ip, port))
        sock.listen(1)
        return sock

    def sock_data_handler(self,sock):
        conn_threads = []
        while True:
            """when a connection occurs, return connection and address"""
            connection, address = sock.accept()
            print("%s - connected" % str(address))
            print("thread_count:%s" % str(len(conn_threads)+1))
            """pass connection and address into the message handler"""
            conn_threads.append(Thread(target=self.message_handler,args=(connection,address)).start())

    def sock_message_handler(self,connection):
        """set size of expected header message field"""
        header_msg_size_field = 8
        """set size of expected header crc field"""
        header_crc_field = 32
        """set size of entire header"""
        header_size = header_msg_size_field + header_crc_field
        complete_message = ""
        header_not_found = True
        while True:
            try:
                """if there is not data continue to loop looking for data"""
                data = connection.recv(40)
                if not data:
                    break
                """there is data in the receive buffer"""
                """append data to message"""
                complete_message += data.decode("utf-8")

                """if we don't have the header information"""
                if header_not_found and len(complete_message) > header_size:
                    """get the length of the incoming message from the header"""
                    message_len = int(complete_message[:header_msg_size_field])
                    """get the crc from the header"""
                    message_crc = complete_message[header_msg_size_field:header_size]
                    if message_len and message_crc: header_not_found = False
                if not header_not_found:
                    """if we have the header information"""
                    """if the data in our message minus our header size is equal to or greater than our header_msg_size"""
                    if len(complete_message) - header_size >= message_len:
                        message = complete_message[header_size:header_size+message_len]
                        print(f"full message received:{message}")
                        crc_md5 = hashlib.md5(bytes(message,"utf-8")).hexdigest()
                        print(f"full message crc match:{crc_md5 == message_crc}")
                        """prepare next message if buffer is overflowed"""
                        complete_message = complete_message[header_size + message_len:]
                        header_not_found = True
                        # """echo the message back to the client"""
                        # self.echo_message(message,connection)
            except Exception as ex:
                print(ex)
                break


    """add observer to our subscription set"""
    def subscribe(self, listener):
        listener._subscribed_to.append(self)
        if listener not in self.message_listeners:
            self.message_listeners.append(listener)
        print("\n%s subscribed to %s" % (listener.__name__,self.__name__))

    """remove observer from our subscription set"""
    def unsubscribe(self, listener):
        listener._subscribed_to.remove(self)
        self.message_listeners.remove(listener)
        print("\n%s unsubscribed to %s" % (listener.__name__,self.__name__))

    """notify_subscribers"""
    def notify_listeners(self,message):
        for listener in self.message_listeners:
            listener.update(message,self)


class Observable(object):
    def __init__(self,name):
        self._subscribed_to = []
        self.__name__ = name

    def join_channel(self,connection,data):
        print("join_channel")
        channel = data["commands"]["join_channel"]["channel"]
        if channel not in self.channel_dict:
            self.channel_dict[channel] = []
            print("\ncreated_list")
        """check input validation"""
        self.channel_dict[channel].append(connection)
        print("\nadded connection to channel")

        response_message = {
            "type": "response",
            "response_type": "reply",
            "response": {
                "request_id":data["request_id"],
                "message": "True"
            }
                         }
        return str(response_message)

    def listen(self,hosting_if_ip,port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((hosting_if_ip, port))
        sock.listen(1)
        return sock

    # def socket_data_handler(self,sock):
    #     conn_threads = []
    #     while True:
    #         connection, address = sock.accept()
    #         print("%s - connected" % str(address))
    #         print("thread_count:%s" % str(len(conn_threads)+1))
    #         conn_threads.append(Thread(target=self.connection_handler,args=(connection,address)).start())

    # def connection_handler(self,connection,address):
    #     header_msg_size_field = 8
    #     header_crc_field = 32
    #     header_size = header_msg_size_field + header_crc_field
    #     complete_message = ""
    #     header_not_found = True
    #     while True:
    #         try:
    #             """if there is not data continue to loop looking for data"""
    #             data = connection.recv(40)
    #             if not data:
    #                 break
    #             """there is data in the receive buffer"""
    #             """append data to message"""
    #             complete_message += data.decode("utf-8")
    #
    #             """if we don't have the header information"""
    #             if header_not_found and len(complete_message) > header_size:
    #                 """get the length of the incoming message from the header"""
    #                 message_len = int(complete_message[:header_msg_size_field])
    #
    #                 """get the crc from the header"""
    #                 message_crc = complete_message[header_msg_size_field:header_size]
    #
    #                 if message_len and message_crc: header_not_found = False
    #
    #             if not header_not_found:
    #                 """if we have the header information"""
    #
    #                 """if the data in our message minus our header size is equal to or greater than our header_msg_size"""
    #                 if len(complete_message) - header_size >= message_len:
    #                     message = complete_message[header_size:header_size+message_len]
    #
    #                     print(f"full message received:{message}")
    #                     crc_md5 = hashlib.md5(bytes(message,"utf-8")).hexdigest()
    #                     print(f"full message crc match:{crc_md5 == message_crc}")
    #
    #                     """prepare next message if buffer is overflowed"""
    #                     complete_message = complete_message[header_size + message_len:]
    #                     header_not_found = True
    #                     """echo the message back to the client"""
    #                     self.echo_message(message,connection)
    #                     """send message through handler"""
    #                     self.request_handler(message, connection, address)
    #         except Exception as ex:
    #             print(ex)
    #             break

    # def echo_message(self,message,connection):
    #     header_size_field = 8
    #     header_crc_field = 32
    #     """echo the clients message back to them"""
    #     response_message = {
    #         "type": "response",
    #         "response_type": "echo",
    #         "response": message
    #                      }
    #     crc_md5 = hashlib.md5(bytes(str(response_message),"utf-8")).hexdigest()
    #     message = f"{len(str(response_message)):<{header_size_field}}{crc_md5}" + str(response_message)
    #     self.send_message(message,connection)

    # def send_message(self,message,connection):
    #     print(f"Observable Sending Message:{message}")
    #     connection.sendall(bytes(message,"utf-8"))

    # def request_handler(self,request_message,connection,address):
    #     print("\nmessage_handler:%s - data received:%s:" % (address,request_message))
    #     try:
    #         data = json.loads(request_message.replace("\'", "\""))
    #         print(json.dumps(data,indent=4))
    #         if 'join_channel' in data['commands']:
    #             response = self.join_channel(connection,data)
    #             self.send_channel(channel=data["commands"]["join_channel"]["channel"],message=response)
    #         # elif 'send_channel' in data:
    #         #     self.send_channel(data["send_channel"]["channel"],data["send_channel"]["message"])
    #     except Exception as ex:
    #         print(ex)
    #         response = {"exception":str(ex)}
    #         connection.sendall(str(response).encode())
    #
    # def send_channel(self,channel,message):
    #     for subscriber in self.channel_dict[channel]:
    #         subscriber.sendall(bytes(message, "utf-8"))

if __name__ == "__main__":
    #com_handler = Thread(target=CommunicationHandler, args=("192.168.1.37", 7337)).start()
    com_handler = CommunicationHandler("192.168.1.37", 7337)
    observable_a = Observable(name="observable_a")
    com_handler.onThread(CommunicationHandler.subscribe(observable_a))
    # print("1")
    #
    # print("next")
    #conn_threads.append(Thread(target=CommunicationHandler, args=(connection, address)).start())
    #com_handler = CommunicationHandler(hosting_if_ip="192.168.1.37",port=7337)
    #print('COM HANDLER STARTED')
    #observable_a = Observable(name="observable_a")

    #com_handler.subscribe(observable_a)