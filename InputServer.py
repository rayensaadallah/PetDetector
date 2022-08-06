import json
import socket
import schedule
import time

class InputServer:
    listConnectedSocker = []
    port = 1024

    def __int__(self, user, name, x, y, width, height):
        self.user = user
        self.name = name  # name ta3 spot
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def initializ(self,port):
        serverTcpSocket = "127.0.0.1"

        port += 1
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if (server.connect_ex((serverTcpSocket, port)) == 0):
            InputServer.onError(0)
            pass
        else:
            server.bind((serverTcpSocket, port))
            server.listen(5)

            client, address = server.accept()
            return client

    def onNewSocket(userName, listConnectedSocker):
        if (userName not in listConnectedSocker):
            listConnectedSocker.append(userName)
        else:
            InputServer.onError(3)



    def onMessageRecived(self, client):
        objectRecived = client.recv(1024)  # cheniya hal 1024 : hiya buffer -> speed haja ki haka ?

        return objectRecived

    def onMessageRecivedForever(self):        #he4i zedteha bch truni forever
                                              # kont nejm ne7i fonction he4i wjuste nekte while true f fonction onMessageRecived
        try:
            schedule.every(5).seconds.do(InputServer.onMessageRecived)
            while 1 :
                schedule.run_pending()
                time.sleep(1)
        except:
            InputServer.onError(1)



    def onError(errorNumber, client):
        match errorNumber:
            case 0:
                client.send(bytes("this port already used", "utf-8"))
            case 1:
                client.send(bytes("server disconnected", "utf-8"))
            case 2 :
                client.send(bytes("invalid data", "utf-8"))
            case 3 :
                client.send(bytes("user already", "utf-8"))
            case default:
                client.send(bytes("other Problem", "utf-8"))


    def processMessage(self, objectRecived):

        dictObject = json.loads(objectRecived)  # {"name": "kitchen", "x": 50, "y": 60, "width": 200, "height": 100, "user": "ismail" }
        name = dictObject["name"]
        x = dictObject["x"]
        y = dictObject["y"]
        width = dictObject["width"]
        height = dictObject["height"]

        if( (x < 0) or (y < 0) or (width < 0) or (height < 0)or (width > 1920) or (height > 1080) or (name == "") ):
            InputServer.onError(2)
        else:
            return [name, x, y, width, height]





#server.close() ma3raftech win n7oteha